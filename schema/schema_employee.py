from database.model_employee import ModelEmployee
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType


class EmployeeAttribute:
    name = graphene.String(description='Name of Role')
    hired_on = graphene.DateTime(description='Hired_on date')
    department_id = graphene.Int(description='ID of Department')
    role_id = graphene.Int(description='ID of Role')


class Employee(SQLAlchemyObjectType, EmployeeAttribute):
    class Meta:
        model = ModelEmployee
        interfaces = (relay.Node,)


Model = ModelEmployee
