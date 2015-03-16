from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'itbook.db')

db = SQLAlchemy(app)

from book.views import book_blueprint
app.register_blueprint(book_blueprint)

db.create_all()

