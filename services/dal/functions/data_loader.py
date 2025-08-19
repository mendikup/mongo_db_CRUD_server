from interfaces.dal_interface import IData_loader


class Data_loader(IData_loader):

    def __init__(self):
        self.collection = None

    def get_aii_data(self):
        return self.collection.find({})

    def Write_new_soldier(self,id,first_name,last_name,phone_number,rank):
        anser = self.collection.insert_one({
            'ID':id,
            'first_name':first_name,
            'last_name':last_name,
            'phone_number':phone_number,
            'rank':rank
            })
        return anser.acknowledged

    def update_by_id(self,id,filde:dict):
        modified_count = self.collection.update_one({'ID':id},{'$set':filde}).modified_count
        return modified_count > 0

    def delete_by_id(self,id):
        deleted_count = self.collection.delete_one({'ID':id}).deleted_count
        return deleted_count > 0