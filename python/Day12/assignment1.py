#sort the collections customers  on  name in desc and list the top 5 records
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
 
mydb = myclient["harsha"]
 
mycol = mydb["customers"]
 
mydoc = mycol.find().sort("name", -1).limit(5)
#mydoc = mycol.find().sort("name", pymongo.DESCENDING).limit(5) #both works as same
 
for x in mydoc:
  print(x)