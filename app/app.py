from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError
from datetime import date
from flask_cors import *


class JSONEncoder(_JSONEncoder):
    # default是被递归调用的，只要是遇到不能被序列化的，就会继续调用
    def default(self, o):
        # 把对象转换为字典，__init__类的变量是不会被存在__dict__,实例变量不会存在于这里面。例如init里面的
        # 一个对象不可以用o['name']的方式访问变量，但是如果给它增加__getitem__方法后就可以，
        # getattr获取对象下面的对应值，getattr（o，item）
        # 当有keys属性，和__getitem__方法时才返回
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        # if isinstance(o, date):
        #     return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/dev-api/v1')


def register_plugin(app):
    """
    注册第三方插件
    :param app:
    :return:
    """
    from app.models.base import db
    db.init_app(app)
    # 在上下文语境中才能
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True, resources=r'/*')
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    # 第三方插件注册到flask核心对象上
    register_blueprints(app)
    register_plugin(app)

    return app