#  -*- coding:  utf-8 -*-
#  __author__:  梁绕绕
#  2021/1/20 9:24


from app.models.base import Base
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Message(Base):
    id = Column(Integer, primary_key=True)
    es_description = relationship('EsDescription')
    mid = Column(Integer, ForeignKey('es_description.id'))
    message = Column(String(500))
