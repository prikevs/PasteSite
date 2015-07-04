#coding:utf8

from flask import render_template, request, abort, url_for, redirect, flash
from . import app
from .models import Paste, create_paste
from .forms import PasteForm
from .utils import showcode

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasteForm(request.form)
    if request.method == 'POST' and form.validate():
            paste = create_paste(form.poster.data, form.syntax.data,
                             form.content.data)
            return redirect(url_for('show', post_id=paste.id))

    return render_template('index.html', form=form)

    


@app.route('/<int:post_id>')
def show(post_id):
    paste = Paste.query.filter_by(id=post_id).first()
    if paste == None:
        abort(404)

    return render_template('show.html', 
            poster=paste.poster,
            post_time=paste.post_time,
            content=showcode(paste.content, paste.syntax))

