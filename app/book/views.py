from os import path

from flask import Blueprint
from flask import render_template
from flask import redirect

from search_form import SearchForm
from app.api.book import BookApi


book_blueprint = Blueprint('book', __name__)
base_url = 'http://it-ebooks-api.info/v1'


@book_blueprint.route('/')
def index():
    return 'hello'


@book_blueprint.route('/book/<string:id>')
def get_book(id):
    api = BookApi()
    book = api.get_book_by_id(id)

    return render_template('book-details.html', book=book)


@book_blueprint.route('/books/<string:keywords>')
@book_blueprint.route('/books/<string:keywords>/page/<string:number>')
def search_books(keywords, number=1):
    api = BookApi()
    books, pagination = api.search_books(keywords, number)
    return render_template('books.html', books=books, pagination=pagination, keywords=keywords)


@book_blueprint.route('/search', methods=['GET', 'POST'])
def do_search():
    form = SearchForm()
    if form.validate_on_submit():
        redirect_url = path.join('/books', form.data['keywords'])
        return redirect(redirect_url)

    return render_template('home.html', form=form)


@book_blueprint.route('/record/<string:keywords>')
def record(keywords):
    api = BookApi()
    api.record(keywords)

    return 'record successful'


@book_blueprint.route('/pagination')
@book_blueprint.route('/pagination/<int:page>')
def pagination(page=1):
    api = BookApi()
    paginator = api.pagination(page)

    print paginator.has_next
    print paginator.has_prev
    print paginator.next_num
    print paginator.prev_num
    for book in paginator.items:
        print book

    return render_template('paginator.html', paginator=paginator)
