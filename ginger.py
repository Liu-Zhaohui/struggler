from app.app import create_app
from app.libs.error_code import ServerError
from app.libs.errors import APIException
from werkzeug.exceptions import HTTPException

app = create_app()

@app.errorhandler(Exception)
def framework_errpr(e):
    # flask 1.0 可以捕获所有异常
    if isinstance(e, APIException):
        return e

    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 做一个日志log的记录
        # 这样可读性不是很好，因此再定义一个ServerError()
        # 调试模式,显示详细信息，否则，返回我们定义的json错误信息
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e
        return ServerError()

if __name__ == '__main__':
    app.run(debug=True)
