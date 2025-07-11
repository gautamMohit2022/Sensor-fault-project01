from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
url = "mongodb+srv://gautampm2006:%23ILOVEMYCOUNTRY@cluster0.lwlizjm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connectt to server
client = MongoClient(url)

#create database name and collection name
DATABASE_NAME="SESNORFAULTDETECTION"
COLLECTION_NAME='wafer-fault'

df = pd.read_csv("K:/PWSKILLS/PROJECTS/SENSOR FAULT DETECTION/notebooks/wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)