import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
 
mydb = myclient["harsha"]
 
mycol = mydb["customers"]
 
x = mycol.find_one()
 
print(x)