# Title: WEB335 Assignment 8.3 Python in Action
# Date: December 19, 2021
# Description: This exercise's objective is to use 
#Python to create a new user document in the web335 database using python
#Source: Arora, Lakshay. August 21, 2020. Query a MongoDB Database using PyMongo!. url: https://www.analyticsvidhya.com/blog/2020/08/query-a-mongodb-database-using-pymongo/


#Import pymongo, pprint, and datetime
from pymongo import MongoClient
import pprint
import datetime

#connect to localhost port 27017
client = MongoClient('localhost', 27017) 
#Connect to the web335 mongo database
db = client.web335

#create a new user 
user = {
    "first_name": "Baxter",
    "last_name": "Burgundy",
    "employee_id": "500006",
    "email": "bark@news5.com",
    "date": datetime.datetime.utcnow() 
}

user_id = db.users.insert_one(user).inserted_id
print(user_id)
pprint.pprint(db.users.find_one({"employee_id": "500006"}))

