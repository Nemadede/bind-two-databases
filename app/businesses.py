from sqlalchemy import Column, Integer, String

from app import Business_Base


class Business(Business_Base):
    __tablename__: str = "businesses"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    email = Column(String(255), unique=True)

    def __init__(self, name, email, country):
        self.name = name
        self.email = email
        self.country = country