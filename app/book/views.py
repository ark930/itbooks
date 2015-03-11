# -*- coding: utf-8 -*-
from os import path

from flask import Blueprint
from flask import render_template
from flask import redirect
import requests

from models import Book
from pagination import Pagination
from search_form import SearchForm


book_blueprint = Blueprint('book', __name__)

base_url = 'http://it-ebooks-api.info/v1'

@book_blueprint.route('/')
def index():
    return 'hello'


@book_blueprint.route('/book/<int:id>')
def get_book(id):
    request_url = path.join(base_url, 'book')
    request_url = path.join(request_url, str(id))
    r = requests.get(request_url)

    data = r.json()
    if data['Error'] == '0':
        book = Book(**data)
        return render_template('book-details.html', book=book)

    return do_error(data['Error'])


@book_blueprint.route('/books/<string:keywords>')
@book_blueprint.route('/books/<string:keywords>/page/<int:number>')
def get_books(keywords, number=1):
    request_url = path.join(base_url, 'search')
    request_url = path.join(request_url, keywords)

    if number != 1:
        request_url = path.join(request_url, 'page')
        request_url = path.join(request_url, str(number))

    r = requests.get(request_url)
    data = r.json()
    if data['Error'] == '0':
        if int(data['Total']) > 0:
            books = []
            for b in data['Books']:
                book = Book(**b)
                books.append(book)

            pagination = Pagination((int(data['Page'])+10)/10, 10, int(data['Total']))
            return render_template('books.html', books=books, pagination=pagination, keywords=keywords)
        else:
            return 'No data'

    return do_error(data['Error'])


@book_blueprint.route('/search', methods=['GET', 'POST'])
def do_search():
    form = SearchForm()
    if form.validate_on_submit():
        redirect_url = path.join('/books', form.data['keywords'])
        return redirect(redirect_url)

    return render_template('/home.html', form=form)


def do_error(error_no):
    return '发生错误：Error=' + error_no




