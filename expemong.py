import pymongo
import sys
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Expences"]
mycol = mydb["expcoll"]

code = raw_input('Enter Code :')
name = raw_input('Enter Name :')
expe = raw_input('Enter Expe :')
date = raw_input('Enter Date :')

x = mycol.insert_one({code:"code",name:"name",expe:"expe",date:"date"})
mydb.myclient.save()
#print(x.inserted_id)
Y = mycol.find()
print(Y)
