from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, decode_token
import sqlite3
import logging
from datetime import timedelta
from functools import wraps

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Change this in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Configure logging
logging.basicConfig(filename='auth.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger('').addHandler(console)

# Initialize SQLite database (persistent)
def init_db():
    conn = sqlite3.connect('users.db', check_same_thread=False)  # Persist data
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT,
                        role TEXT)''')
    conn.commit()
    return conn

db_conn = init_db()

def register_user(username: str, password: str, role: str) -> bool:
    conn = db_conn
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    if cursor.fetchone():
        return False
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_pw, role))
    conn.commit()
    return True

def authenticate_user(username: str, password: str):
    conn = db_conn
    cursor = conn.cursor()
    cursor.execute("SELECT password, role FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    if not result or not bcrypt.check_password_hash(result[0], password):
        logging.info(f"Failed authentication attempt for user: {username}")
        return False
    logging.info(f"Successful authentication for user: {username}")
    return create_access_token(identity={"username": username, "role": result[1]})

def validate_token(token: str):
    try:
        return decode_token(token)["sub"]  # Extract identity
    except Exception:
        logging.info("Invalid or expired token attempt")
        return False

def reset_password(username: str, new_password: str) -> bool:
    conn = db_conn
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    if not cursor.fetchone():
        return False
    hashed_pw = bcrypt.generate_password_hash(new_password).decode('utf-8')
    cursor.execute("UPDATE users SET password=? WHERE username=?", (hashed_pw, username))
    conn.commit()
    return True

def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            identity = get_jwt_identity()
            if identity and identity.get("role") in [required_role, "admin"]:
                return f(*args, **kwargs)
            return jsonify({"msg": "Access denied"}), 403
        return wrapper
    return decorator

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if register_user(data["username"], data["password"], data.get("role", "user")):
        return jsonify({"msg": "User registered successfully"}), 201
    return jsonify({"msg": "User already exists"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    token = authenticate_user(data["username"], data["password"])
    if token:
        return jsonify({"access_token": token}), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/reset-password', methods=['POST'])
def reset():
    data = request.json
    if reset_password(data["username"], data["new_password"]):
        return jsonify({"msg": "Password reset successful"}), 200
    return jsonify({"msg": "User not found"}), 404

@app.route('/user-dashboard', methods=['GET'])
@jwt_required()
def user_dashboard():
    return jsonify({"msg": "Welcome to the user dashboard!"}), 200

@app.route('/admin-dashboard', methods=['GET'])
@jwt_required()
@role_required("admin")
def admin_dashboard():
    return jsonify({"msg": "Welcome to the admin dashboard!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
