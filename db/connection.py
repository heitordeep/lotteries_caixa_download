import os

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from log_generator import RegisterLogs

logger = RegisterLogs()

URI = os.getenv('URI')
DATABASE = os.getenv('DATABASE')


class Database:
    def __init__(self):
        self.client = MongoClient(f'mongodb://{URI}:27017/{DATABASE}')
        self.db = self.client[DATABASE]

    def find_content(self, query, collection, limit=0, skip=0):

        try:
            documents = self.db[collection].find(query, limit=limit, skip=skip)
            documents = list(documents)
            logger.debug_register(
                f'Reading {len(documents)} records of the {collection} documents!'
            )

            contens_null = ['NaN', 'nan', ' ']

            # Remove ObjectId in _id and Nan.
            for i in range(len(documents)):
                if str(documents[i]['Cidade']) in contens_null:
                    documents[i]['Cidade'] = 'null'
                if str(documents[i]['UF']) in contens_null:
                    documents[i]['UF'] = 'null'

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
