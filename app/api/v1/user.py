from flask import jsonify
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required  # 这个要跟在路由下面，要不然无法进入verify_password 环节
def get_user(uid):
    # id 用get_or_404
    user = User.query.get_or_404(uid)
    return jsonify(user)
