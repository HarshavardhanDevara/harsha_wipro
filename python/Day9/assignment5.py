import MySQLdb
#pip install mysqlclient
#after pip it is working fine
try:
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="Harsha@1807#",
        db="rps"
    )
    print("Connected successfully")
    mydb.close()
except MySQLdb.Error as e:
    print(f"Error: {e}")
