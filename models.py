from schemas import UserBase, CustomerDetails
from database import Base
from sqlalchemy import Column, Float, Integer, String


# create a user table 
class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    userid = Column(String)
    password = Column(String)
    contact = Column(Integer)


def create_table(request: UserBase):
    tabl = type(
        "OwnerTable",
        (Base,),
        {
            "__tablename__": request.userid,
            "id": Column(Integer, primary_key=True, index=True),
            "name": Column(String),
            "quantity": Column(Integer),
            "price": Column(String),
        },
    )


def create_customers_table(request: UserBase):
    tabl = type(
        "CustomerTable",
        (Base,),
        {
            "__tablename__": request.userid + "customers",
            "id": Column(Integer, primary_key=True, index=True),
            "name": Column(String),
            "contact": Column(Integer),
            "shopvalue": Column(Float),
        }
    )
