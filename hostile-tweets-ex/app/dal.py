from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
database_url = os.getenv("MONGO_URL")
client = MongoClient(database_url)
db = client["IranMalDB"]
collection = db["tweets"]

def get_tweets():
    cursor = collection.find()
    data = pd.DataFrame(list(cursor))
    return data
