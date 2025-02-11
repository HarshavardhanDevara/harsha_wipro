import sqlite3
 
# Use 'with' to connect to the SQLite database
 
with sqlite3.connect('rps_database.db') as con:
 
    # Create a cursor object
    cursor = con.cursor()
 
    # Write the SQL command to select all records from the Students table
    query = "SELECT * FROM Students;"
 
    # Execute the SQL command
    cursor.execute(query)
 
    # Fetch all records
    all_students = cursor.fetchall()
 
    # Display results in the terminal
    print("All Students:\n\n")
 
    for student in all_students:
        print(student)
 