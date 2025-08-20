from fastapi import FastAPI
from services.dal.functions.data_loader import Data_loader

app = FastAPI()
dal = Data_loader()
@app.get("/")
def root():
    return {"ok": True}

@app.get("/get_all_data")
def get_all_data():
   res = dal.get_all_data()
   return res

@app.post("/insert_new_soldier")
def insert_new_soldier(data:dict):
    res = dal.insert_new_soldier(
        data["id"],
        data["first_name"],
        data["last_name"],
        data["phone_number"],
        data["rank"]

    )
    return {"status": res}

@app.put("/update_by_id")
def update_by_id(data:dict):
    res = dal.update_by_id(
        data["id"],
        data["filed"]
    )
    return {"status": res}


@app.delete("/delete_by_id")
def delete_by_id(data:dict):
    res = dal.delete_by_id(
        data["id"]
    )
    return {"status": res}
