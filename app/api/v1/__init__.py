from flask import Blueprint
from app.api.v1 import user, book, client, token, es_des

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    #红图里面优化掉
    # user.api.register(bp_v1, url_prefix='/user')
    # book.api.register(bp_v1, url_prefix='/book')

    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    es_des.api.register(bp_v1)

    return bp_v1
