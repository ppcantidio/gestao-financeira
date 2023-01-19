import os
import pymongo
from dynaconf import settings


class Database:
    def __init__(self, collection):
        self.client = pymongo.MongoClient(settings["MONGO_CONNECTION"])
        self.db = self.client.get_database(settings["MONG_DB_NAME"])
        self.collection = self.db.get_collection(collection)
