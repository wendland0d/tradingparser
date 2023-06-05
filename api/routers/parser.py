from fastapi import APIRouter

from .parsers import buff


parser = APIRouter(prefix="/parser")

parser.include_router(buff.router)