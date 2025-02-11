import sqlite3

# Use 'with' to connect to the SQLite database and automatically close the connection when done
with sqlite3.connect('my_database.db') as connection:

    # Create a cursor object
    cursor = connection.cursor()

    # Write the SQL command to create the Students table
    str = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    );
    '''

    # Execute the SQL command
    cursor.execute(str)

    # Commit the changes
    connection.commit()

    # Print a confirmation message
    print("Students table created successfully!")