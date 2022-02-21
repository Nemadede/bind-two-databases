import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base

User_Base = declarative_base()
Business_Base = declarative_base()
main_app = FastAPI()

from app.users import *
from app.businesses import *
from app.db_connection import user_engine, business_engine

User_Base.metadata.create_all(bind=user_engine)
Business_Base.metadata.create_all(bind=business_engine)

from app.test_queries import create_user

# create_user("nema", "dede", "nema6dede@gmail.com", "AppsTechLabs", "cameroon")

if __name__ == '__main__':
    uvicorn.run("main:main_app", reload=True)
