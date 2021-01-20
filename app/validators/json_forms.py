#  -*- coding:  utf-8 -*-
#  __author__:  梁绕绕
#  2021/1/20 14:27


import wtforms
from wtforms import validators
# from wtforms.validators import ValidationError
from wtforms_tornado import Form

class EsDescriptionForm(Form):
    title = wtforms.StringField('title',  [validators.Length(min=4, max=23)])

    # def validate_title(self, field):
    #     if field.data != 'hello world':
    #          raise ValidationError(u'Must be hello world')