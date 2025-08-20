class Soldier:

    def __init__(self ,ID,first_name,last_name,phone_number,rank):
        self.ID =ID
        self.first_name =first_name
        self.last_name =last_name
        self.phone_number =phone_number
        self.rank =rank


    def __str__(self):
        return f"solider details - ID: {self.ID} || first name: {self.first_name} || last name: {self.last_name} || phone number: {self.phone_number} || rank: {self.rank}"





