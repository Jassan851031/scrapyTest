from pymongo import MongoClient

def insertData(arr):

    client = MongoClient("mongodb+srv://admin:admin1234@myCluster.kqvdy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.comunas_info
    collection = db.comunas_fases
    collection.insert_many(arr)

