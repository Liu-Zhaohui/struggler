from wtforms import StringField, IntegerField, ValidationError
from wtforms.validators import DataRequired, length, Email, Regexp

from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validators.base import BaseForm as Form
from app.validators.base import BaseJsonForm as JsonFom


class ClientForm(Form):
    account = StringField(validators=[DataRequired(message='account不可用空'), length(min=5,max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    #用来验证客户端传过来的type是否是枚举值；数字转化为了枚举类型,client是枚举类型
    def validate_type(self, value):
        try:
            # value从请求传过来，value是IntergerField类型，value.data取值
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        #type是IntegerField类型，client是一个实际的值，因此要self.type.data
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='邮箱格式不正确')])
    # "secret": "a12d3435", {6, 22}多个空格死活验证不通过，
    secret = StringField(validators=[DataRequired(message='密码不可用空'),
                                     Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(message='昵称不可为空'),
                                       length(min=2,max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError

    def validate_nickname(self, value):
        if User.query.filter_by(nickname=value.data).first():
            raise ValidationError


class EsDescriptionForm(JsonFom):

    title = StringField(validators=[DataRequired(message='title不可用空')])
    category = StringField(validators=[DataRequired(message='分类不可用空')])