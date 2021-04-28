from pymongo import MongoClient

# URL = "mongodb://localhost:8080"
# USER = "admin"
# PASS = "admin1234"

def insertData(arr) {

    client = MongoClient("mongodb+srv://admin:admin1234@myCluster.kqvdy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.comunas_info
    collection = db.comunas_fases
    collection.insert_many(arr)
}