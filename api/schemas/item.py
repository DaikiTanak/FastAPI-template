from typing import Optional

from pydantic import BaseModel, Field


class ItemGetResponse(BaseModel):
    item_id: int
    name: str
    price: int


class ItemPostRequest(BaseModel):
    name: str
    price: int
    description: Optional[str] = Field(None, example="item description")


class ItemPostResponse(BaseModel):
    item_id: int
    creation_status: bool
