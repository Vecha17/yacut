from wtforms.validators import ValidationError

from yacut.consts import URL_SYMBOLS
from yacut.models import URLMap


class Validate_short():
    """
    Проверяет введёный пользователем короткий id на наличие его в бд
    и на содержание в коротком id разрешённых символов.
    """

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        short_id = field.data
        if URLMap.query.filter_by(short=short_id).first() is not None:
            raise ValidationError(
                field.gettext(
                    'Предложенный вариант короткой ссылки уже существует.'
                )
            )
        for symbol in short_id:
            if symbol not in URL_SYMBOLS:
                raise ValidationError(
                    field.gettext(
                        'Указано недопустимое имя для короткой ссылки.'
                    )
                )


class Validate_original():
    """
    Проверяет ссылку на наличие её в бд.
    """
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        original_link = field.data
        if URLMap.query.filter_by(original=original_link).first() is not None:
            raise ValidationError(
                    field.gettext(
                        'Эта ссылка уже имеет сокращённую версию.'
                    )
                )
