from pymongo import MongoClient
import os

class Conector():
    def __init__(self):
        self.addres = "mongodb://localhost:27017"
        self.db_name = "enemy_soldiers"
        self.collection_name = "soldier_details"


    def connect(self):
        self.client = MongoClient(self.addres)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def close(self):
        self.client.close()
        self.db = None
        self.collection = None


