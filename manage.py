#  -*- coding:  utf-8 -*-
#  __author__:  梁绕绕
#  2021/1/20 10:08

from flask_script import Manager
from app.app import create_app
from app.models.base import db
# from app.models import *
#
# manager = Manager(app)
# migrate = Migrate(app, db)
# manager.add_command('db', MigrateCommand)
#
#
# if __name__ == '__main__':
#     manager.run()

from flask_migrate import Migrate, MigrateCommand

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
from app.models.es_message import Message
from app.models.es_description import EsDescription
manager.add_command('db', MigrateCommand)
manager.run()