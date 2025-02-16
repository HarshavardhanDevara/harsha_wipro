#sort the collections customers  on  name in desc and list the top 5 records
import pymongo
 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
 
mydb = myclient["harsha"]
 
mycol = mydb["restaurants"]
 
mydoc = mycol.find().sort("name").limit(2)
#mydoc = mycol.find().sort("name", pymongo.DESCENDING).limit(5) #both works as same
 
for x in mydoc:
  print(x)
