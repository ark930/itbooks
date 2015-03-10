from flask import Blueprint

book_blueprint = Blueprint('book', __name__)


@book_blueprint.route('/home')
def home():
    return 'home'