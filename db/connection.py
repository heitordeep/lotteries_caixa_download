from decouple import config
from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient(
            f'mongodb://{config("MONGO_URI")}:27017/{config("MONGO_DATABASE")}'
        )
        self.db = self.client[config('MONGO_DATABASE')]
        self.collection = self.db[config('COLLECTION')]

    def find_content(self, limit=0, skip=0):
        return self.collection.find({})

    def insert(self, content):
        new_content = {'$set': content}
        return self.collection.update_one(content, new_content, upsert=True)
