import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",                        #need to give ip: 127.0.0.1 in place of localhost in sometime
  port=3306,                               #port required in some cases only
  user="root",
  password="Harsha@1807#",
  database="rps"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("CREATE TABLE customers (name VARCHAR(15), address VARCHAR(15))")