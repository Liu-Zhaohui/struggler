from flask import current_app, jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from app.models.user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }

    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data)

    expiration = current_app.config['TOKEN_EXPIRTATION']
    # token是个字符串，我们要求所有的试图函数返回都是json，因此将其变成字典，序列化器生成的token不是普通的字符串，它是个byte类型字符串，因此
    #要使用decode转换下
    token = generate_auth_token(identity['UID'],
                        form.type.data,
                        None,
                        expiration)

    t = {
        'token': token.decode('ascii')
    }

    # 需要被序列化！！！重要重要
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    """
    :param uid:  用户id
    :param ac_type:   客户端类型
    :param scope:  作用域
    :param expiration: 过期旗舰
    :return:
    """
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    # 字符串
    return s.dumps({
        'uid': uid,
        'type': ac_type.value
    })
