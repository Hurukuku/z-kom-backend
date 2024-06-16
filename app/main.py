from fastapi import FastAPI


from .routers import items, users
from . import models
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


app.include_router(items.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}

