from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    sub_title = db.Column(db.String(128))
    description = db.Column(db.String(1024))
    author = db.Column(db.String(32))
    isbn = db.Column(db.String(13))
    year = db.Column(db.CHAR(4))
    page = db.Column(db.CHAR(6))
    publisher = db.Column(db.String(32))
    image = db.Column(db.String(256))
    download = db.Column(db.String(256))

    def __init__(self, **args):
        for key, val in args.items():
            if key == 'ID':
                self.id = val
            elif key == 'Title':
                self.title = val
            elif key == 'SubTitle':
                self.sub_title = val
            elif key == 'Description':
                self.description = val
            elif key.lower() == 'isbn':
                self.isbn = val
            elif key == 'Author':
                self.author = val
            elif key == 'Year':
                self.year = val
            elif key == 'Page':
                self.page = val
            elif key == 'Publisher':
                self.publisher = val
            elif key == 'Image':
                self.image = val
            elif key == 'Download':
                self.download = val

    def __repr__(self):
        return "Book %s: '%s'" % (self.id, self.title)