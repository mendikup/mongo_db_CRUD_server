from interfaces.dal_interface import IData_loader
from db_connector import Conector

class Data_loader(IData_loader):

    def __init__(self):
        self.connector = Conector()
        self.connector.connect()
        self.collection = self.connector.collection


    def get_all_data(self)->list:
        return list(self.collection.find({},{'_id':False}))

    def insert_new_soldier(self,id:int,first_name:str,last_name:str,phone_number:str,rank:str)->bool:
        res = self.collection.insert_one({
            'ID':id,
            'first_name':first_name,
            'last_name':last_name,
            'phone_number':phone_number,
            'rank':rank
            })
        return res.acknowledged

    def update_by_id(self,id:int,filde:dict)->bool:
        modified_count = self.collection.update_one({'ID':id},{'$set':filde}).modified_count
        return modified_count > 0

    def delete_by_id(self,id:int)->bool:
        deleted_count = self.collection.delete_one({'ID':id}).deleted_count
        return deleted_count > 0