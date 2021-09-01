from pydantic import BaseModel, Field
import datetime


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