from pymongo.mongo_client import MongoClient

class DBconnector:

    def __init__(self):
       self.client = MongoClient("mongodb://localhost:27017")

    def get_connection(self,db_name,db_collection):
        db = self.client[db_name]
        collection = db[db_collection]
        return collection

