import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Harsha@1807#",
  database="rps"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("SHOW TABLES")
 
for x in mycursor:
  print(x)