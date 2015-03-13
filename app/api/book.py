from .base import ItbooksApiBase
from .error import ItbookApiError
from app.models.book import Book
from app.book.pagination import Pagination


class BookApi(ItbooksApiBase):
    def get_book_by_id(self, id):
        r = self._get('book/%s' % id)
        data = r.json()

        if data['Error'] == '0':
            return Book(**data)

        raise ItbookApiError(data['Error'])

    def search_books(self, keywords, number):
        r = self._get('search/%s/page/%s' % (keywords, number))
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