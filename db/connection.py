import os

from decouple import config
from pymongo import MongoClient
from pymongo.errors import BulkWriteError, ConnectionFailure

from log_generator import RegisterLogs

logger = RegisterLogs()

URI = os.getenv('URI')
PORT = os.getenv('PORT')
DATABASE = os.getenv('DATABASE')


class Database:
    def __init__(self):
        self.client = MongoClient(f'mongodb://{URI}:{PORT}/{DATABASE}')
        self.db = self.client[DATABASE]

    def find_content(self, collection, limit=0, skip=0):

        try:
            documents = self.db[collection].find({}, limit=limit, skip=skip)
            documents = list(documents)
            logger.debug_register(
                f'Reading {len(documents)} records of the {collection} documents!'
            )

            # Remove ObjectId in _id and Nan.
            for i in range(len(documents)):
                if str(documents[i]['Cidade']) == 'nan':
                    documents[i]['Cidade'] = ''
                if '_id' in documents[i]:
                    documents[i]['_id'] = str(documents[i]['_id'])

            return documents

        except ConnectionFailure as e:
            logger.error_register(f'Error: {e._message}')
            return {'Error: ': e._message}

    def insert(self, collection, content):

        try:

            return self.db[collection].insert_many(content)

        except ConnectionFailure as e:
            logger.error_register(f'Error: {e._message}')
            return {'Error': e._message}

    def drop(self, collection):

        try:

            return self.db[collection].drop()

        except ConnectionFailure as e:
            logger.error_register(f'Error: {e._message}')
            return {'Error': e._message}
