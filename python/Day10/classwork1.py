import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Harsha@1807#",
  database="rps"
)
 
mycursor = mydb.cursor()  # cursor is an  object to execute sql statements
 
 
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
 
val = ("John", "Highway 21")
 
mycursor.execute(sql, val)
 
mydb.commit()
 
print(mycursor.rowcount, "record inserted.")