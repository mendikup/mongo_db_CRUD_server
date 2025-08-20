from fastapi import FastAPI
from services.dal.functions.data_loader import Dataloader

app = FastAPI()
dal = Dataloader()
@app.get("/")
def root():
    return {"ok": True}

@app.get("/get_all_data")
def get_all_data():
   res = dal.get_all_data()
   return res