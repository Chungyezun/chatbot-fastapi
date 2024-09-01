from fastapi import FastAPI, APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/Chat", response_class=HTMLResponse)
async def ChatPage(request: Request):
    return templates.TemplateResponse("chat.html", context={"request": request})