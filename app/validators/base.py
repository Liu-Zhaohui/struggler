from wtforms import Form
from app.libs.error_code import ParameterException
from flask import request


class BaseForm(Form):

    def __init__(self):
        data = request.json
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self


class BaseJsonForm(Form):

    def __int__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(BaseJsonForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseJsonForm, self).validate()
        if not valid:
            # form errors
            raise ParameterException(msg=self.errors)
        return self
