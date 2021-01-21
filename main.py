import uuid
import random
from dataclasses import dataclass

from fastapi import FastAPI, Header
from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str


@dataclass
class Item:
    id: int
    name: str
    price: int


app = FastAPI()


@app.post("/login")
def login(user: User):
    return dict(id=random.randrange(1, 100), token=str(uuid.uuid4()))


@app.get("/products")
def products(token: str = Header(None)):
    items = list()
    items.append(Item(id=1, name="Apple", price=5000 * (0.9 if token else 1)))
    items.append(Item(id=2, name="Orange", price=8000 * (0.9 if token else 1)))
    items.append(Item(id=3, name="banana", price=3000 * (0.9 if token else 1)))

    return items
