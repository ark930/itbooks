from .base import ItbooksApiBase
from .error import ItbookApiError
from app.models.book import Book
from app.book.pagination import Pagination
from app import db
from sqlalchemy.exc import IntegrityError


class BookApi(ItbooksApiBase):
    def get_book_by_id(self, id):
        r = self._get('book/%s' % id)
        data = r.json()

        if data['Error'] == '0':
            return Book(**data)

        raise ItbookApiError(data['Error'])

    def search_books(self, keywords, page=1):
        r = self._get('search/%s/page/%s' % (keywords, page))
        data = r.json()

        if data['Error'] == '0':
            if int(data['Total']) > 0:
                books = []
                for b in data['Books']:
                    book = Book(**b)
                    books.append(book)

                pagination = Pagination((int(data['Page'])+10)/10, 10, int(data['Total']))
                return books, pagination
            else:
                return ItbookApiError('No data')

        raise ItbookApiError(data['Error'])

    def record(self, keywords):
        pagination = self.save_data(keywords, 1)

        while pagination.has_next:
            pagination = self.save_data(keywords, pagination.page+1)

        db.session.commit()

    def pagination(self, page):
        paginator = Book.query.paginate(page, 10, True)

        return paginator

    def save_data(self, keywords, page):
        books, pagination = self.search_books(keywords, page)
        for b in books:
            print b
            self.db_insert(b)

        return pagination

    def db_insert(self, data):
        if Book.query.filter_by(id=data.id).first() is None:
            db.session.add(data)
        else:
            print 'except'


