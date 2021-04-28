from pymongo import MongoClient

URL = "mongodb://localhost:8080"
USER = "dmin"
PASS = "admin1234"

client = MongoClient("mongodb+srv://admin:admin1234@myCluster.kqvdy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.comunas_info
collection = db.comunas_fases


test = {
    "nombre": "Raul"
}

collection.insert_one(test)