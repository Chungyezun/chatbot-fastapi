from fastapi import FastAPI, APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import List
from pydantic import BaseModel

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str

messages = ["Hello World!"]

@router.get("/Chat", response_class=HTMLResponse)
async def ChatPage(request: Request):
    return templates.TemplateResponse("chat.html", context={"request": request})

@router.get("/api/messages", response_model=List[str])
async def get_messages():
    return messages

@router.post("/api/messages", response_model=str)
async def post_message(msg: Message):
    if not msg.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    messages.append(msg.message)
    return msg.message
