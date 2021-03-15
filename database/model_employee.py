from .base import Base
from .model_department import ModelDepartment
from .model_role import ModelRole
from sqlalchemy import (
    Column, DateTime, ForeignKey, Integer, String, func
)
from sqlalchemy.orm import backref, relationship


class ModelEmployee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    role_id = Column(Integer, ForeignKey('roles.id'))
    department = relationship(
        ModelDepartment,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))
    role = relationship(
        ModelRole,
        backref=backref('roles',
                        uselist=True,
                        cascade='delete,all'))
