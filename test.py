from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"

@app.get("/home/{name}")
def read_name(name:str):
  return {"name": name}

@app.get("/home/{name}")
def read_name_error(name:int):
  return {"name": name}

@app.get("/models/{model_name}")
def get_model(model_name:ModelName):
  if model_name is ModelName.alexnet:
    return {"model_name": model_name, "message": "Alexnet!"}
  if model_name.value == "resnet":
    return {"model_name": model_name, "message": "Resnet!"}