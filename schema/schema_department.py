from database.model_department import ModelDepartment
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType


class DepertmentAttribute:
    name = graphene.String(description='Name of Department')


class Department(SQLAlchemyObjectType, DepertmentAttribute):
    class Meta:
        model = ModelDepartment
        interfaces = (relay.Node,)


Model = ModelDepartment
