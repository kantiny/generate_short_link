from aiohttp import web

from generate_short_link.utils import handle_json_error
from main import app


@app.router.post("/get_tasks")
@handle_json_error
async def get_tasks(request: web.Request) -> web.Response:
    post = await request.json()
    input_json = post["input_json"]

    return web.json_response(
        {
            "status": "ok",
            "data": input_json,
        }
    )
