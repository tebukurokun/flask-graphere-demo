from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphene import relay
import graphene
from . import schema_department
from . import schema_role
from . import schema_employee
from database import base


class InsertEmployee(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        department = graphene.String(required=True)
        role = graphene.String(required=True)

    employee = graphene.Field(lambda: schema_employee.Employee)

    def mutate(self, info, name, department, role):
        department = schema_department.Model(name=department)
        base.db_session.add(department)
        role = schema_role.Model(name=role)
        base.db_session.add(role)

        employee = schema_employee.Model(
            name=name, department=department, role=role)
        base.db_session.add(employee)

        base.db_session.commit()
        return InsertEmployee(employee=employee)


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    employee = graphene.Field(lambda: schema_employee.Employee,
                              name=graphene.String())
    employee_list = SQLAlchemyConnectionField(schema_employee.Employee)
    department_list = SQLAlchemyConnectionField(schema_department.Department)
    role_list = SQLAlchemyConnectionField(schema_role.Role)

    def resolve_employee(self, info, name):
        query = schema_employee.Employee.get_query(info)
        result = query.filter(schema_employee.Model.name == name).first()
        return result


class Mutation(graphene.ObjectType):
    insert_employee = InsertEmployee.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
