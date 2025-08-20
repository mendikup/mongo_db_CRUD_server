import pymongo
from services.dal.functions.db_connector import DBconnector


class Dataloader:

    def __init__(self):
        self.connector = DBconnector()
        self.db_name = "mydb"
        self.db_collection = "soldiers"
        self.collection = self.connector.get_connection(self.db_name, self.db_collection)


    def get_all_data(self):
        data = (list(self.collection.find({},{"_id":False})))
        return data


    # def load_data(self):
    #     db_name = "mydb"
    #     db_collection = "soldiers"
    #     collection = self.connector.get_connection(db_name, db_collection)
    #
    #     # retrieves all documents from the collection
    #     soldiers = collection.find({},{"_id":False}).limit(10)
    #
    #     for soldier in soldiers:
    #         soldier = SoldierBuilder.build_soldier(soldier)
    #         print(soldier)




#
# dl = Dataloader()
# dl.load_data()