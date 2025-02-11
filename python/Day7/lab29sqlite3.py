import sqlite3
 
try:
    with sqlite3.connect("my.db") as conn:
        print("Opened SQLite database  successfully.")
 
except sqlite3.OperationalError as e:
   print("Failed to open database:", e)