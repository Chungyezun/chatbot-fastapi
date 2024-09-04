from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import chat

app = FastAPI()

app.mount('/static', StaticFiles(directory="static"), name="static")
app.include_router(chat.router)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app)