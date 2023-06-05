from . import AsyncSession
from sqlalchemy import select

from models.models import Item

async def select_all_by_parser(session: AsyncSession, parser: str):
    q = select(Item).filter(Item.parser_name == parser)
    result = await session.execute(q)
    return result.scalars()