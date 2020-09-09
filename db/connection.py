from decouple import config
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


class Database:
    def __init__(self):
        self.client = MongoClient(
            f'mongodb://{config("MONGO_URI")}:27017/{config("MONGO_DATABASE")}'
        )
        self.db = self.client[config('MONGO_DATABASE')]

    def find_content(self, collection, limit=0, skip=0):

        try:
            documents = self.db[collection].find({}, limit=limit, skip=skip)
            documents = list(documents)

            # Remove ObjectId in _id and Nan.
            for i in range(len(documents)):
                if str(documents[i]['Cidade']) == 'nan':
                    documents[i]['Cidade'] = ''
                if '_id' in documents[i]:
                    documents[i]['_id'] = str(documents[i]['_id'])
               
            return documents

        except ConnectionFailure as e:
            return {'Error: ': e._message}

    def insert(self, collection, content):

        try:
            new_content = {'$set': content}
            return self.db[collection].update_one(
                content, new_content, upsert=True
            )
        except ConnectionFailure as e:
            return {'Error': e._message}
