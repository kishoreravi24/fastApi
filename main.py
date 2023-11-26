from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"Hello":"world"}


@app.get("/itmes/{item_id}")
def read_item(item_id: int):
    return {"item_id":item_id}

@app.put("/items/{item_id}")
def update_item(item_id:int,item:Item):
    return {"item_name":item.name,"item_id":item_id}
