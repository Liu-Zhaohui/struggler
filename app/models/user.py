from sqlalchemy import Column, Integer, SmallInteger,String
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.base import Base, db
from app.libs.error_code import NotFound, AuthFaild
import datetime

class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=True)
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)
    time = datetime.date(2020, 7, 12)
    _password = Column('password', String(100))

    def keys(self):
        # 字典的键
        return ['id', 'email', 'nickname', 'auth', 'time']



    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, paw):
        self._password = generate_password_hash(paw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            # password = secret
            ##重点重点
            user.password = secret
            # user._password = generate_password_hash(secret)
            db.session.add(user)

    @staticmethod
    def verify(email, secret):
        user = User.query.filter_by(email=email).first_or_404()
        # if not user:
        #     raise NotFound(msg='user not found')
        if not user.check_password(secret):
            raise AuthFaild()

        return {'UID': user.id}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)