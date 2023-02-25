from typing import Optional

from fastapi import FastAPI

api_service = FastAPI()


@api_service.get("/")
def read_root():
    return {"Hello": "World"}


@api_service.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
