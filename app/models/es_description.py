#  -*- coding:  utf-8 -*-
#  __author__:  梁绕绕
#  2021/1/20 9:18
from app.models.base import Base
from sqlalchemy import Integer, Column, String


class EsDescription(Base):
    __tablename__ = 'es_description'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    category = Column(String(50))
    update_time = Column(Integer)


    @staticmethod
    def get_des_list():
        deslists = EsDescription.query.all()
        return deslists