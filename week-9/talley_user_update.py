# Title: WEB335 Assignment 8.3 Python in Action
# Date: December 19, 2021
# Description: This exercise's objective is to use 
#Python to update the user document created in assignment 9.2

#Import pymongo, pprint, and datetime
from pymongo import MongoClient
import pprint
import datetime

#connect to localhost port 27017
client = MongoClient('localhost', 27017) 
#Connect to the web335 mongo database
db = client.web335

#update the user document (change the email address)

db.users.update_one(
    {"employee_id": "500006"},
    {
        "$set":{
            "email": "wtalley@my365.bellevue.edu"
        }
    }
)

#Using findOne function to output email, employee_id, first_name, and last_name
pprint.pprint(db.users.find_one({"employee_id": "500006"}))
