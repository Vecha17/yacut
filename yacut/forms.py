from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL

from yacut.consts import MIN_LENGTH, MAX_LENGTH_ORIGINAL, MAX_LENGTH_SHORT
from yacut.validators import Validate_short, Validate_original


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная сылка',
        validators=[
            DataRequired('Обязательное поле'),
            Length(MIN_LENGTH, MAX_LENGTH_ORIGINAL),
            URL(),
            Validate_original()
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(MIN_LENGTH, MAX_LENGTH_SHORT, 'Указано недопустимое имя для короткой ссылки'),
            Validate_short()
        ]
    )
    submit = SubmitField('Создать')
