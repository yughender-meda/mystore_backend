from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    userid: str
    password: str
    contact: int


class GetUser(BaseModel):
    username: str
    password: str


class ItemBase(BaseModel):
    name: str
    quantity: int
    price: float
    metric: str


class DeleteItem(BaseModel):
    name: str
    metric: str


class CustomerDetails(BaseModel):
    cust_name: str
    contact: int
    shopvalue: float


class ForQuantity(BaseModel):
    name: str
    metric: str
    quantity: int


class GetPrice(BaseModel):
    itemname: str
    metric: str
