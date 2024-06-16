from sqlalchemy.orm import Session

from . import models, schemas

# Users
def get_user_by_id(db: Session, user_id: int):
    return db.select(models.User).where(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.select()
#Items
def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.User.id == item_id).first()

def get_items(db: Session, category: str | None = None):
    if category:
        return db.query(models.Item).filter(models.Item.category == category)
    else: 
        return db.query(models.Item)
    
def add_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
