import os
from contextlib import asynccontextmanager
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.database import engine
from src.models import BaseModel

# Importamos los routers desde nuestros módulos
from src.example.router import router as example_router

load_dotenv()

ENV = os.getenv("ENV")
ROOT_PATH = os.getenv(f"ROOT_PATH_{ENV.upper()}")


@asynccontextmanager
async def db_creation_lifespan(app: FastAPI):
    BaseModel.metadata.create_all(bind=engine)
    yield


app = FastAPI(root_path=ROOT_PATH, lifespan=db_creation_lifespan)

# Asociamos los routers a nuestra app
app.include_router(example_router)

# Definimos una ruta para la raíz
@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI application!"}
