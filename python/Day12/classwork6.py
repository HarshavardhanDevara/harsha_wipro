import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
 
mydb = myclient["harsha"]
 
mycol = mydb["customers"]
 
mydoc = mycol.find().sort("name")
 
for x in mydoc:
  print(x)