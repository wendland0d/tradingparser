from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from ...depends import get_session, AsyncSession
from models.models import Item, Parser
from models.schemas import (
    ParserItemsResponseModel,
    BaseItemResponseModel,
)
from ...crud import (select_all_by_parser)

router = APIRouter(prefix="/buff")

@router.get("/items", response_model=ParserItemsResponseModel, tags=["parsers"])
async def get_items(session: AsyncSession = Depends(get_session)):
    result = await select_all_by_parser(session=session, parser="buff")
    return ParserItemsResponseModel(parser="buff",
                                    items=[BaseItemResponseModel(hash_name=item.hash_name, price=item.price, count=item.count, lasttime=item.time) for item in result])
    