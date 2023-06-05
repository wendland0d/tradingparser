from .routers.parser import parser
from . import app

app.include_router(parser)