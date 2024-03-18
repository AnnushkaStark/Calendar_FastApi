from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from fastapi import FastAPI

from src.models import *

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

app = FastAPI()