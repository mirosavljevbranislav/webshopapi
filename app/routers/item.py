from uuid import uuid4

from fastapi import Body, APIRouter

from app import app
from app.models.item import Item, ItemSchema

router = APIRouter()


@router.get("/items")
def get_items():
    items = app.db.find()
    item_list = [i for i in items]
    return item_list


@router.get("/items/{item_id}")
def get_item(item_id: str):
    item = app.db.find_one({"_id": item_id})
    if item:
        return item
    return {"Message": "Item not found!"}


@router.post("/items")
def store_to_database(item: ItemSchema):
    item_dict = item.dict()
    item_dict["_id"] = str(uuid4())
    app.db.insert(item_dict)
    return Item(**item_dict)


@router.delete("/items/{item_id}")
def delete_item(item_id: str):
    item = app.db.find_one({"_id": item_id})
    app.db.remove(item)
    return {"Message": f"Item {item['name']} removed successfully!"}


@router.put("/items/{item_id}")
def update_item(item_id: str, what_to_update: str = Body(..., embed=True), value_for_update=Body(..., embed=True)):
    if what_to_update == "price":
        value_for_update = float(value_for_update)
    app.db.update_one({"_id": item_id},
                      {"$set": {what_to_update: value_for_update}})
    return {f"{what_to_update} updated to {value_for_update}"}