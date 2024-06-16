from fastapi import FastAPI
from .routers import items
from . import models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(items.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
