from http import HTTPStatus

from flask import jsonify, request

from . import app, db

from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.views import get_uniqгe_short_id
from yacut.consts import URL_SYMBOLS, MAX_LENGTH_SHORT


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage(
            'Отсутствует тело запроса',
            status_code=HTTPStatus.BAD_REQUEST
        )
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if URLMap.query.filter_by(original=data['url']).first() is not None:
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.',
            status_code=HTTPStatus.BAD_REQUEST
        )
    if 'custom_id' in data:
        short_link = data['custom_id']
        for symbol in short_link:
            if symbol not in URL_SYMBOLS:
                raise InvalidAPIUsage(
                    'Указано недопустимое имя для короткой ссылки',
                    status_code=HTTPStatus.BAD_REQUEST
                )
        if len(short_link) > MAX_LENGTH_SHORT:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки',
                status_code=HTTPStatus.BAD_REQUEST
            )
        if URLMap.query.filter_by(short=short_link).first() is not None:
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.',
                status_code=HTTPStatus.BAD_REQUEST
            )
    else:
        short_link = get_uniqгe_short_id()
    url = URLMap(
        original=data['url'],
        short=short_link
    )
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if url:
        return jsonify(url.to_dict_get_method()), HTTPStatus.OK
    raise InvalidAPIUsage(
        'Указанный id не найден', status_code=HTTPStatus.NOT_FOUND
    )
