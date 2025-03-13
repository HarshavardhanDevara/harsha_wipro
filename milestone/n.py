from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
import sqlite3
import logging
from datetime import timedelta
from functools import wraps

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Change this in production
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)  # Token expires after 30 minutes

# Initialize extensions
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Configure logging
logging.basicConfig(
    filename='auth.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def init_db():
    # Connect to a file-based SQLite database (persistent)
    conn = sqlite3.connect('usersnew.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT,
                        role TEXT)''')
    conn.commit()
    return conn

db_conn = init_db()

# Helper functions
def register_user(username: str, password: str, role: str = "user") -> bool:
    """
    Registers a new user with the provided username, password, and role.
    """
    conn = db_conn
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    if cursor.fetchone():
        logging.warning(f"Registration failed: User {username} already exists.")
        return False
    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_pw, role))
    conn.commit()
    logging.info(f"User {username} registered successfully.")
    return True

def authenticate_user(username: str, password: str) -> str | bool:
    """
    Authenticates a user and returns a JWT token if successful.
    """
    conn = db_conn
    cursor = conn.cursor()
    cursor.execute("SELECT password, role FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    if not result or not bcrypt.check_password_hash(result[0], password):
        logging.warning(f"Authentication failed for user: {username}")
        return False
    logging.info(f"Authentication successful for user: {username}")
    # Create token with username as identity and role in additional claims
    access_token = create_access_token(
        identity=username,
        additional_claims={"role": result[1]}
    )
    return access_token

def validate_token(token: str) -> dict | bool:
    """
    Validates a JWT token and returns the decoded payload if valid.
    """
    try:
        decoded = decode_token(token)
        logging.info(f"Token validated for user: {decoded['sub']}")
        return decoded
    except Exception as e:
        logging.error(f"Invalid or expired token attempt: {e}")
        return False

def reset_password(username: str, new_password: str) -> bool:
    """
    Resets a user's password.
    """
    conn = db_conn
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    if not cursor.fetchone():
        logging.warning(f"Password reset failed: User {username} not found.")
        return False
    hashed_pw = bcrypt.generate_password_hash(new_password).decode('utf-8')
    cursor.execute("UPDATE users SET password=? WHERE username=?", (hashed_pw, username))
    conn.commit()
    logging.info(f"Password reset successful for user: {username}")
    return True

# Role-based access control decorator
def role_required(required_role: str):
    """
    Decorator to enforce role-based access control.
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims["role"] == required_role or claims["role"] == "admin":
                return f(*args, **kwargs)
            logging.warning(f"Access denied for user: {get_jwt_identity()}")
            return jsonify({"msg": "Access denied"}), 403
        return wrapper
    return decorator

# API Endpoints
@app.route('/register', methods=['POST'])
def register():
    """
    Registers a new user.
    """
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return jsonify({"msg": "Missing username or password"}), 400

    if register_user(data["username"], data["password"], data.get("role", "user")):
        return jsonify({"msg": "User registered successfully"}), 201
    return jsonify({"msg": "User already exists"}), 400

@app.route('/login', methods=['POST'])
def login():
    """
    Authenticates a user and returns a JWT token.
    """
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return jsonify({"msg": "Missing username or password"}), 400

    token = authenticate_user(data["username"], data["password"])
    if token:
        return jsonify({"access_token": token}), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/reset-password', methods=['POST'])
def reset():
    """
    Resets a user's password.
    """
    data = request.json
    if not data or "username" not in data or "new_password" not in data:
        return jsonify({"msg": "Missing username or new_password"}), 400

    if reset_password(data["username"], data["new_password"]):
        return jsonify({"msg": "Password reset successful"}), 200
    return jsonify({"msg": "User not found"}), 404

@app.route('/user-dashboard', methods=['GET'])
@jwt_required()
def user_dashboard():
    """
    Example endpoint for user dashboard.
    """
    identity = get_jwt_identity()
    logging.info(f"User {identity} accessed the user dashboard.")
    return jsonify({"msg": "Welcome to the user dashboard!"}), 200

@app.route('/admin-dashboard', methods=['GET'])
@jwt_required()
@role_required("admin")
def admin_dashboard():
    """
    Example endpoint for admin dashboard.
    """
    identity = get_jwt_identity()
    logging.info(f"Admin {identity} accessed the admin dashboard.")
    return jsonify({"msg": "Welcome to the admin dashboard!"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)