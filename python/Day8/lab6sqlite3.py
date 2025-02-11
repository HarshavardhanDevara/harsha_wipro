import sqlite3
 
# Use 'with' to connect to the SQLite database and automatically close the connection when done
 
with sqlite3.connect('rps_database.db') as con:
 
    # Create a cursor object
 
    cursor = con.cursor()
 
    # Write the SQL command to create the Students table
 
    stmt = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    ); '''
 
    # Execute the SQL command
    cursor.execute(stmt)
 
    # Commit the changes
    con.commit()
 
    # Print a confirmation message
    print("Table 'Students' created successfully!")