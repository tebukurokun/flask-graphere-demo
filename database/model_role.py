from .base import Base
from sqlalchemy import Column, Integer, String


class ModelRole(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String)
