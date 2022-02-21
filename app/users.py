from sqlalchemy import Column, Integer, String

from app import User_Base


class User(User_Base):

    __tablename__: str = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True)

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


