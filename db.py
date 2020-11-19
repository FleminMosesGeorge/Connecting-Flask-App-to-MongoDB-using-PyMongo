from flask import Flask
from flask_pymongo import pymongo
from app import app

#CONECTION_STRING = "mongodb+srv://flemin:<password>@democluster.tee0t.mongodb.net/<dbname>?retryWrites=true&w=majority"
CONECTION_STRING = "mongodb+srv://flemin:flemin@democluster.tee0t.mongodb.net/brand_db?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONECTION_STRING)
db = client.get_database('brand_db')
brandnames = db.brand_names
