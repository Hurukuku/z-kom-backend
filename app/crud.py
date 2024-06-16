from sqlalchemy.orm import Session
from .dependencies import get_password_hash
from . import models, schemas

# Users
def get_users(db: Session):
    return db.query(models.User)

def get_user_pass(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first().hashed_password

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(password = hashed_password, email= user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



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
