import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Harsha@1807#",
  database="rps"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("SELECT name, address FROM customers")
 
myresult = mycursor.fetchall()
 
for x in myresult:
  print(x)