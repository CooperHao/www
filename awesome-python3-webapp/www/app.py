import logging; logging.basicConfig(level=logging.INFO)
from datetime import datetime
from aiohttp import web

async def index(request):
    return web.Response(text="Awesome")

app = web.Application()
app.add_routes([web.get('/', index)])  
web.run_app(app)