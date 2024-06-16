from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class ItemBase(BaseModel):
    name: str
    price: int
    category: str
    desc: str | None = None


class OrderBase(BaseModel):
    pass

class UserBase(BaseModel):
    email: str | None = None


class Item(ItemBase):
    id: int
    photos: list[str] = []
    sale: int | None = None

    class Config:
        orm_mode = True

class ItemCreate(ItemBase):
    pass

class OrderCreate(OrderBase):
    items: list[Item]
    owner_id: int


class Order(OrderBase):
    id: int
    items: list[Item]
    owner_id: int
    status: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    orders: list[Order]

    class Config:
        orm_mode = True
        
class UserDB(User):
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    
Order.model_rebuild()
