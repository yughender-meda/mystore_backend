from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_URL = "sqlite:///./store_db.db"
engine = create_engine(SQL_URL, connect_args={"check_same_thread": False})
Sessionl = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = Sessionl()
    try:
        yield db
    finally:
        db.close()
