from flask_wtf import Form
from wtforms import StringField


class SearchForm(Form):
    keywords = StringField('keywords')