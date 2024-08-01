import random

from flask import redirect, render_template

from yacut import app, db
from yacut.forms import URLForm
from yacut.models import URLMap
from yacut.consts import URL_SYMBOLS, SHORT_URL_LENGTH


def get_uniqгe_short_id():
    short_link = ''
    symbols = random.choices(URL_SYMBOLS, k=SHORT_URL_LENGTH)
    for symbol in symbols:
        short_link += symbol
    if URLMap.query.filter_by(short=short_link).first() is not None:
        short_link = get_uniqгe_short_id()
    return short_link


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        if form.custom_id.data:
            short_id = form.custom_id.data
        else:
            short_id = get_uniqгe_short_id()
            form.custom_id.data = short_id
        url = URLMap(
            original=original_link,
            short=short_id
        )
        db.session.add(url)
        db.session.commit()
    return render_template('make_url.html', form=form,)


@app.route('/all')
def all_urls():
    urls = URLMap.query.all()
    return render_template('all_urls.html', urls=urls)


@app.route('/<string:short>')
def short_url_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url.original)
