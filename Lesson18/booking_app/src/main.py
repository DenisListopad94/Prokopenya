import random
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def random_numbers():
    result_numbers = []
    for val in range(6):
        result_numbers.append(random.randint(0, 10))
    return result_numbers


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/{item_id}/{name}")
def get_item_different_types(item_id: int, name: str,) -> dict:
    return {"item_id": item_id, "name": name}


@app.get("/items")
def get_query_types(id_: int, name: str,) -> dict:
    return {"item_id": id_, "name": name}

