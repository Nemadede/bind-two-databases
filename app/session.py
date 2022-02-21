from sqlalchemy.orm import sessionmaker

from app import User, Business
from app.db_connection import user_engine, business_engine

Session = sessionmaker(twophase=True)
Session.configure(binds={User: user_engine, Business: business_engine})