# from flask import Blueprint

from app.libs.redprint import Redprint
# book = Blueprint('book', __name__)
api = Redprint('book')

@api.route('/get')
def get_book():
    return 'get book'