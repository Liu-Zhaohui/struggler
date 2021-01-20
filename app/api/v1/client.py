from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User

from app.validators.forms import ClientForm, UserEmailForm


api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    # 优化代码request.json,移动到构造方法中
    # data = request.json
    # form = ClientForm()
    # if form.validate_for_api():记住，重写了这里以后，就不需要if来判断了
    # form.validate_for_api()
    form = ClientForm().validate_for_api()  # 要返回一个form

    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email,
    }
    promise[form.type.data]()
    # 我们可以预知的错误类型，
    # 未知异常 1 /0   AOP思想，在全局的地方处理位置异常

    return Success()

def __register_user_by_email():
    # 一定要data=的方式传递,优化代码后，ClientForm中构造方法传了data= request.json后，就不用传了
    # form = UserEmailForm()
    # form.validate_for_api()
    form = UserEmailForm().validate_for_api()
    User.register_by_email(
        form.nickname.data,
        form.account.data,
        form.secret.data)