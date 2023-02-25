from fastapi import APIRouter
from typing import Optional

import api.schemas.item as item_schema

router = APIRouter()

@router.get("/items/{item_id}", response_model=item_schema.ItemGetResponse)
def read_item(item_id: int, q: Optional[str]):
    # Request to DB
    return item_schema.ItemGetResponse(
        item_id=item_id,
        name="mock",
        price=10000
    )

@router.post("/items/", response_model=item_schema.ItemPostResponse)
def create_item(item_body: item_schema.ItemPostRequest):
    # Request to DB
    return item_schema.ItemPostResponse(item_id=0, creation_status=True)