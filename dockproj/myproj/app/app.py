#assignment
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to SQLite3
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route to test database
@app.route('/')
def home():
    return "Welcome to Flask with SQLite!"

# Route to fetch data from SQLite
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in users])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
