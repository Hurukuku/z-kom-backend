from pydantic import BaseModel


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

class CreateOrder(OrderBase):
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


Order.model_rebuild()
