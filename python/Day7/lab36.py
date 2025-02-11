import sqlite3
 
 
# Use 'with' to open and close the connection automatically
 
with sqlite3.connect('my_database.db') as conn:
 
    cursor = conn.cursor()
 
    # List of records to insert
 
    records = [
    ("muni", 24 ,"muni@gamil.com"),
    ("hari", 25 ,  "hari@gmail.com"),
    ("bindu", 21 ,"bindu@gmail.com")
]
 
# Insert multiple records using executemany()
cursor.executemany("INSERT INTO Students (name, age ,email ) VALUES (?, ?, ?)", records)
 
# Commit and close
conn.commit()
print("Fake student records inserted successfully!")
conn.close()