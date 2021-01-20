from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from flask import current_app, g
from app.libs.error_code import AuthFaild
from collections import namedtuple

auth = HTTPBasicAuth()
###HTTPBasicAuth 要求账号密码在headers中传递，key=Authorization, value =basic base64(account:secret)
# User = namedtuple('User', ['uid', 'actype', 'scope'])# 这个地方就写错了，参数都要一样？
User = namedtuple('User', ['uid', 'ac_type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    if not user_info:
        return False
    else:
        g.user = user_info
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        #用来解密token，字符串转化为字典
        data = s.loads(token)
    except BadSignature:
        raise AuthFaild(msg='token is invalid',
                        error_code='1002')
    except SignatureExpired:
        raise AuthFaild(msg='token is expired',
                        error_code='1003')
    uid = data['uid']
    ac_type = data['type']
    return User(uid, ac_type, '')
