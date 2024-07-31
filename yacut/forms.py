from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL

from yacut.validators import Validate_short, Validate_original


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная сылка',
        validators=[
            DataRequired('Обязательное поле'),
            Length(1, 256),
            URL(),
            Validate_original()
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(1, 16, 'Указано недопустимое имя для короткой ссылки'),
            Validate_short()
        ]
    )
    submit = SubmitField('Создать')
