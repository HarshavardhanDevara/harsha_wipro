import sqlite3

# Create and connect to the SQLite database
conn = sqlite3.connect("/home/harsha/Desktop/python/myproj/app/database.db")  # The database file will be created here
cursor = conn.cursor()

# Create the 'users' table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)''')

# Insert some initial data into the 'users' table
cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob')")
conn.commit()  # Commit the changes to the database

# Close the database connection
conn.close()

print("Database initialized and sample data inserted!")
