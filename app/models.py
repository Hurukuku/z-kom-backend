from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    
    orders = relationship("Order", back_populates="owner")
    # items = relationship("Item", back_populates="owner")

    
class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True)
    isPaid = Column(Boolean, default=False)   
    owner_id = Column(Integer, ForeignKey("users.id"))
    # owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="orders")
    # items = relationship("Item", back_populates="order")


class Item(Base):    
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    category = Column(String)
    desc = Column(String)
    photos = relationship("Photo", back_populates="item")


class Photo(Base):
    __tablename__ = "photos"
    
    id = Column(Integer, primary_key=True)
    src = Column(String)
    item_id = Column(Integer, ForeignKey('items.id'))
    
    item = relationship('Item', back_populates='photos')