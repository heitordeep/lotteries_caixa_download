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

    def find_content(self, query, collection, limit=0):

        try:
            documents = self.db[collection].find(query, limit=limit)
            documents = list(documents)
            logger.debug_register(
                f'Reading {len(documents)} records of the {collection} documents! '
                f'Query -> {query}'
            )

            # Remove ObjectId on _id.
            for i in range(len(documents)):
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
