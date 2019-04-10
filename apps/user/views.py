from flask import Blueprint

web = Blueprint('web', __name__)

@web.route('user/')
def user():


    return 'user'

