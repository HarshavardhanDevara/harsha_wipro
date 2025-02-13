import MySQLdb
 
mydb = MySQLdb.connect(                    
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)
 
mycursor = mydb.cursor()
 
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
 
mycursor.execute(sql, adr)
 
myresult = mycursor.fetchall()
 
for x in myresult:
  print(x)