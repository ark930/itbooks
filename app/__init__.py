from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/itbook.db'
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['WTF_CSRF_ENABLED'] = True

db = SQLAlchemy(app)
db.create_all()

from book.views import book_blueprint
app.register_blueprint(book_blueprint)
