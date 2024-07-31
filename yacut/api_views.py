from flask import jsonify, request

from . import app, db

from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.views import get_uniqгe_short_id
from yacut.consts import URL_SYMBOLS


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage(
            'Отсутствует тело запроса',
            status_code=400
        )
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if URLMap.query.filter_by(original=data['url']).first() is not None:
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.',
            status_code=400
        )
    if 'custom_id' in data:
        short_link = data['custom_id']
        for symbol in short_link:
            if symbol not in URL_SYMBOLS:
                raise InvalidAPIUsage(
                    'Указано недопустимое имя для короткой ссылки',
                    status_code=400
                )
        if len(short_link) > 16:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки',
                status_code=400
            )
        if URLMap.query.filter_by(short=short_link).first() is not None:
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.',
                status_code=400
            )
    else:
        short_link = get_uniqгe_short_id()
    url = URLMap(
            original=data['url'],
            short=short_link
        )
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url:
        return jsonify(url.to_dict_get_method()), 200
    raise InvalidAPIUsage('Указанный id не найден', status_code=404)
