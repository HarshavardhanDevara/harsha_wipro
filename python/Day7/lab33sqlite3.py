# #to delete all records from table
# import sqlite3

# # Use 'with' to open and close the connection automatically
# with sqlite3.connect('my_database.db') as connection:

#     cursor = connection.cursor()

#     # Delete all rows from the Students table
#     delete_query = 'DELETE FROM Students;'
#     cursor.execute(delete_query)

#     # Commit the changes
#     connection.commit()

#     # Print a confirmation message
#     print("All rows deleted successfully!")