import pymongo
import os
from os import path
if path.exists('env.py'):
    import env

MONGODB_URI = os.getenv('MONGO_URI')
DBS_NAME = 'myTestDB'
COLLECTION_NAME = 'myFirstMDB'

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print('Mongo is connected!')
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print('Could not connect to MongoDB: %s') % e

conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

# Insert 1 new record
# new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}
# coll.insert(new_doc)

# Insert many new record
# new_docs = [{'first': 'towa', 'last': 'Piver', 'dob': '11/03/1950', 'gender':'m',
#     'hair_colour': 'pink', 'occupation': 'writer', 'nationality': 'english'},
#     {'first': 'sawi', 'last': 'Sadu', 'dob': '11/03/1982', 'gender':'m',
#     'hair_colour': 'black', 'occupation': 'writer', 'nationality': 'american'}]
# coll.insert(new_docs)

#coll.remove({'first': 'douglas'})

#coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)
