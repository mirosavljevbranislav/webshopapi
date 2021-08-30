import datetime
from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field
from pymongo import MongoClient

app = FastAPI()

CONNECTION_URI = "mongodb+srv://Bangie:1mirosavljev1@cluster0.zcy3e.mongodb.net/test"
client = MongoClient(CONNECTION_URI)
app.db = client.Webshop.Items


class Item(BaseModel):
    id: str = Field(alias="_id")
    name: str
    description: str
    price: float
    created: datetime.datetime


class ItemSchema(BaseModel):
    name: str
    description: str
    price: float
    created: datetime.datetime = Field(default_factory=datetime.datetime.now)


@app.get("/items")
def get_items():
    items = app.db.find()
    item_list = [i for i in items]
    return {"items": item_list}


@app.get("/items/{item_id}")
def get_item(item_id: str):
    item = app.db.find_one({"_id": item_id})
    if item:
        return {"item": item}
    return {"Message": "Item not found!"}


@app.post("/items")
def store_to_database(item: ItemSchema):
    item_dict = item.dict()
    item_dict["_id"] = str(uuid4())
    app.db.insert(item_dict)
    return Item(**item_dict)


@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    item = app.db.find_one({"_id": item_id})
    app.db.remove(item)
    return {"Message": f"Item {item['name']} removed successfully!"}


@app.put("/items/")
def update_item(item_id: str, what_to_update, value_for_update):
    app.db.update_one({"_id": item_id},
                      {"$set": {what_to_update: value_for_update}})
    return {"Message": f"{what_to_update} updated successfully to {value_for_update}"}


if __name__ == '__main__':
    pass
