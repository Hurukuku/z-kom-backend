from sqlalchemy.orm import Session
from app.schemas import Item
from fastapi import APIRouter, Depends, HTTPException
from .. import crud, models, schemas
from ..dependencies import get_db

router = APIRouter()

@router.get('/items', response_model=list[Item])
async def get_items(category: str | None = None, db: Session = Depends(get_db)):
    items = crud.get_items(db, category)
    return items
@router.get('/items/{id}', response_model=Item)
async def get_item(id: int):
    pass

@router.put('/items')
async def add_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    if crud.add_item(db, item):
        return 'Success'
    else:
        raise HTTPException(status_code=500, detail="Error")
