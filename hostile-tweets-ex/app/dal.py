from pymongo import MongoClient

MONGO_URL = "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"
client = MongoClient(MONGO_URL)
db = client["IranMalDB"]
collection = db["tweets"]

a = collection.find_one()
print(a)
