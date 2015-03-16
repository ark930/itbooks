from app import db


class Book2keyword(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    keyword = db.Column(db.String(32), index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))

    def __repr__(self):
        return "<Book2keyword %s => %s>" % (self.book_id, self.keyword)
