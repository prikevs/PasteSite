#coding:utf8

from wtforms import Form, TextAreaField, StringField, SelectField, validators

myChoices = [
    ("text", "Text"),
    ("c", "C"),
    ("c++", "C++"),
    ("python", "Python"),
    ("java", "Java"),
]

class PasteForm(Form):
    poster = StringField('Poster', [validators.Length(max=30), validators.Required()])
    syntax = SelectField('Syntax', choices=myChoices, validators=[validators.Required()])
    content = TextAreaField('Content', [validators.data_required()])

