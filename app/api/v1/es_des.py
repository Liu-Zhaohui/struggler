#  -*- coding:  utf-8 -*-
#  __author__:  梁绕绕
#  2021/1/20 13:40

from flask import request
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.es_description import EsDescription
from app.models.es_message import Message
import json

api = Redprint('es_des')

# 增加描述信息：http://127.0.0.1:5000/v1/es_des/desc
# {
#     "title":"司机常跑路线啊",
#     "category": "run_time啊",
#     "content": "这是内容啊"
# }
@api.route('/add_desc', methods=['POST'])
def insert_es_des():
    req = request.json
    if request.method == 'POST':
        with db.auto_commit():
            es_des = EsDescription()
            es_des.title = req['title']
            es_des.category = req['category']
            db.session.add(es_des)
            # 取des表里面的id
            db.session.flush()

            message = Message()
            message.mid = es_des.id
            message.message = req['content']
            db.session.add(message)

            return 'success'


# 列表接口查询http://127.0.0.1:5000/v1/es_des/deslist
@api.route('/deslist', methods=['GET'])
def deslist():
    dst = EsDescription.get_des_list()
    jsondata = []
    for i in dst:
        result = {}
        result['title'] = i['title']
        result['category'] = i['category']
        result['id'] = i['id']
        jsondata.append(result)
        jsondar = json.dumps(jsondata, ensure_ascii=False)
    return jsondar