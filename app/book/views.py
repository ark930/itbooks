# -*- coding: utf-8 -*-
from os import path

from flask import Blueprint
from flask import render_template
import requests

from models import Book
from pagination import Pagination


book_blueprint = Blueprint('book', __name__)

base_url = 'http://it-ebooks-api.info/v1'


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


# @book_blueprint.route('/book', methods=['POST'])
# def add_book():
# return 'post book'


@book_blueprint.route('/books/<string:keys>')
@book_blueprint.route('/books/<string:keys>/page/<int:number>')
def get_books(keys, number=1):
    request_url = path.join(base_url, 'search')
    request_url = path.join(request_url, keys)

    if number != 1:
        request_url = path.join(request_url, 'page')
        request_url = path.join(request_url, str(number))

    r = requests.get(request_url)

    data = r.json()
    if data['Error'] == '0':
        books = []
        for b in data['Books']:
            book = Book(**b)
            books.append(book)

        print data['Page']
        pagination = Pagination((int(data['Page'])+10)/10, 10, int(data['Total']))
        print pagination.page,  pagination.pages
        for page in pagination.iter_pages():
            print page
        return render_template('books.html', books=books, pagination=pagination)

    return do_error(data['Error'])


def do_error(error_no):
    return '发生错误：Error=' + error_no


def do_pagination(data):
    page_count = (int(data['Total']) + 10) / 10
    now_page = data['Page']



