from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# Response Model's
class BaseItemResponseModel(BaseModel):
    
    hash_name: str = Field(title="Hash Name")
    price: float = Field(title="Price")
    count: int = Field(title="Count")
    lasttime: datetime = Field(title="Last time updated")
    
class ParserItemsResponseModel(BaseModel):
    parser: str = Field(title="Parser")
    items: List[BaseItemResponseModel] = Field(title="Items")