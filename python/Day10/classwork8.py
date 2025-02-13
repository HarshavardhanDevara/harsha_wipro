import mysql.connector
 
mydb = mysql.connector.connect(                    
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)
 
mycursor = mydb.cursor()
 
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
 
mycursor.execute(sql)
 
myresult = mycursor.fetchall()
 
for x in myresult:
  print(x)