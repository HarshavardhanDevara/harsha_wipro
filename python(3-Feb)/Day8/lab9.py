import sqlite3
 
# Use 'with' to connect to the SQLite database
with sqlite3.connect('rps_database.db') as connection:
    cursor = connection.cursor()
 
    # SQL command to update a student's age
    update_query = " UPDATE Students  SET age = ?   WHERE name = ?; "

 
    # Data for the update
    new_age = 29
    student_name = 'harsha'
 
    # Execute the SQL command with the data
    cursor.execute(update_query, (new_age, student_name))
 
    # Commit the changes to save the update
    connection.commit()
 
    # Print a confirmation message
    print(f"Updated age for {student_name} to {new_age}.")