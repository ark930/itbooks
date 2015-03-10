from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/itbook.db'

db = SQLAlchemy(app)
db.create_all()

from book.views import book_blueprint
app.register_blueprint(book_blueprint)


@app.route('/')
def hello():
    return 'hello world'
