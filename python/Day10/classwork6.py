import MySQLdb                             #import mysql.connector
                                            #mydb = mysql.connector.connect
mydb = MySQLdb.connect(                    
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("SELECT * FROM customers")
 
myresult = mycursor.fetchone()
 
print(myresult)