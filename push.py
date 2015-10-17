import json
from pymongo import MongoClient, errors


def client_connection():
    client = MongoClient("127.0.0.1", 27017)
    database = client.database
    return database


def json_push():
    db = client_connection()
    collection = db.collection
    data = {}
    with open('data.json', 'r') as f:   #opens our json file as f parameter
        data = json.load(f)             #loads f to data
        #for row in data:                #prints out entries in data object
            #print(row)
        f.close()                       #closes the file
    collection.insert(data)
    for entry in collection.find():
        print(entry)



json_push()
