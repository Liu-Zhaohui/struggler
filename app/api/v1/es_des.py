#  -*- coding:  utf-8 -*-
#  __author__:  梁绕绕
#  2021/1/20 13:40

from flask import request
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.es_description import EsDescription
from app.models.es_message import Message
import json
from datetime import datetime

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
            es_des.update_time = int(datetime.now().timestamp())
            db.session.add(es_des)
            # 取des表里面的id
            db.session.flush()

            message = Message()
            message.mid = es_des.id
            message.message = json.dumps(req['content'])
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
        result['type'] = i['category']
        result['id'] = i['id']
        result['timestamp'] = i['update_time']
        jsondata.append(result)
        jsondar = json.dumps(jsondata, ensure_ascii=False)
    return jsondar

# http://127.0.0.1:5000/v1/es_des/id
# {
#     "id": 3
# }
# 响应：{"shipperId": 1, "route": {"startId": "110100", "endId": "110100"}}
@api.route('/id', methods=['POST'])
def per_es():
    req = request.json
    if request.method == 'POST':
        id = req['id']
        message = Message.query.filter_by(mid=id).first()
        return message.message


# http://127.0.0.1:5000/v1/es_des/edit
# {
#     "id": 5,
#     "content": "更新内容"
# }
#
@api.route('/edit', methods=['POST'])
def per_edit():
    req = request.json
    if request.method == 'POST':
        with db.auto_commit():
            id = req['id']
            message = Message.query.filter_by(mid=id).first()
            message.message = req['content']
            db.session.add(message)
            return '更新成功'