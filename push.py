import json
import sys
from pymongo import MongoClient, errors

def client_connection():
    client = MongoClient("127.0.1.1", 27017)
    database = client.database
    return database


def parse(filename):
    db = client_connection()
    collection = db.collection
    data = {}
    with open(str(filename[1]), 'r') as f:      #opens our json file as f parameter
        data = json.load(f)             #loads f to data
        #for row in data:                #prints out entries in data object
            #print(row)
        f.close()                       #closes the file
    collection.insert(data)
    for entry in collection.find():
        print(entry)

if __name__ == '__main__':
    parse(sys.argv)
