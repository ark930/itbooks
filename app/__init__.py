from flask import Flask
from book.views import book_blueprint

app = Flask(__name__)
app.register_blueprint(book_blueprint)


@app.route('/')
def hello():
    return 'hello world'