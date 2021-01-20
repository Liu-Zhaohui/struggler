from .errors import APIException

"""
400 请求参数错误
401 未授权
403 禁止访问
404 未找到资源货页面
500 服务器产生位置错误
200 查询成功   201更新，创建成功  204 删除成功
301   302  用来重定向

"""
# class ClientTypeException(HTTPexception):
#     #这样会得出一个html得响应信息
#     code = 400
#     description = {
#         'invalid parameter type'
#     }

class Success(APIException):
    code = 201
    msg = 'SUCCESS'
    error_code = 0

class ServerError(APIException):
    code = 500
    msg = 'we make a mistake(*~~~*)'
    error_code = 999


class ClientTypeError(APIException):
    # 为了解决返回为html的问题，因此自己实现APIException，  code是status， error_code是业务信息错误码
    code = 400
    msg = 'client is valid'
    error_code = 1006

class ParameterException(APIException):
    # 为了解决返回为html的问题，因此自己实现APIException，  code是status， error_code是业务信息错误码
    code = 400
    msg = 'invalid parameter'
    error_code = 1000

class NotFound(APIException):
    code = 404
    msg = 'the resource are not found 0-0...'
    error_code = 1001

class AuthFaild(APIException):
    code = 401
    msg = 'authorization faild'
    error_code = 1005