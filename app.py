from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import chat

app = FastAPI()

app.mount('/static', StaticFiles(directory="static"), name="static")
app.include_router(chat.router)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app)