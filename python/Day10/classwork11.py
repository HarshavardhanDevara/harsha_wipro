import MySQLdb
 
mydb = MySQLdb.connect(                    
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)
 
 
mycursor = mydb.cursor()
 
sql = "SELECT * FROM customers ORDER BY address"
 
mycursor.execute(sql)
 
myresult = mycursor.fetchall()
 
for x in myresult:

  print(x)

 