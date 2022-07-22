import pymongo
import mongo
import json
from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import ReturnDocument
client = MongoClient('localhost',27017)
Hospital = client['Hospital_health']
# #1)----------------Fetching patient details---------------
# print("Fetching details of all patients")
Details_collection = Hospital['Patient_details']
# find_result1 = Details_collection.find({},{"_id":0})
# for x in find_result1:
#     print(x)
# print(find_result1) 

# 2)---------------Finding the number of cases based on a particular date------------------------
# print("Finding the number of cases based on a particular date")
Patient_Collection = Hospital['Monitoring']
# hos_data = {"Date ": "14-07-2022"} 
# find_result = Patient_Collection.find_one(hos_data)
# if find_result != "None":
#     print("details you are looking for is :\n", find_result)
# else:
#     print("unknown date") 
# print("\n") 

# #3)-------------------Finding the results of all Patients who got tested-----------------
# print("Finding the results of all Patients who got tested")
Test_Collection = Hospital['Patient_results']
# mydoc = Test_Collection.find({},{"_id" : 0})
# for x in mydoc:
#       print(x)    
# #4)---------------------Finding the all patients who got tested positive------------------
# myquery = { "Test_result": "Positive" }
# mydoc = Test_Collection.find(myquery,{"_id" : 0, })
# for x in mydoc:
#       print(x)
# #5)-------------------Finding the patients who are in ICU------------
# myquery_1 = {"Allocated_Room": "ICU"}
# for x in Test_Collection.find(myquery_1,{"_id":0}):
#      print(x)
  
# #6)-----------------------Finding patients whose test type is RT-PCR
# myquery_2 = {"Test_Type": "RT-PCR"}
# for x in Test_Collection.find(myquery_2,{"_id":0}):
#     print(x)
   
# #7)-------------------------Finding the patients who are in Critical condition----------
myquery_3 = {" Conditon" : "Critical"}
for x in Test_Collection.find(myquery_3,{"_id":0, "Patient_id":1, "Allocated_Room":1," Conditon":1}):
      print(x) 
 






