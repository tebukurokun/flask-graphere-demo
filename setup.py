from database.model_department import ModelDepartment
from database.model_role import ModelRole
from database.model_employee import ModelEmployee
from database import base
import logging
import sys


log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)


if __name__ == "__main__":
    log.info('Create database')
    base.Base.metadata.create_all(base.engine)

    log.info('Insert data')
    engineering = ModelDepartment(name='Engineering')
    base.db_session.add(engineering)
    hr = ModelDepartment(name='Human Resources')
    base.db_session.add(hr)

    manager = ModelRole(name='manager')
    base.db_session.add(manager)
    engineer = ModelRole(name='engineer')
    base.db_session.add(engineer)

    peter = ModelEmployee(name='Peter', department=engineering, role=engineer)
    base.db_session.add(peter)
    roy = ModelEmployee(name='Roy', department=engineering, role=engineer)
    base.db_session.add(roy)
    tracy = ModelEmployee(name='Tracy', department=hr, role=manager)
    base.db_session.add(tracy)
    base.db_session.commit()
