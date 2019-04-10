from flask import Blueprint, jsonify

from helper import is_isbn_or_key
from yushu_book import YunShuBook

web = Blueprint('web', __name__)

@web.route('book/search/<q>/<page>/')
def search(q, page):
    """
        q: 普通关键字 isbn
        page
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
    	result = YunShuBook.serarch_by_isbn(q)
    else:
    	result = YunShuBook.serarch_by_keyword(q)

    return jsonify(result)

