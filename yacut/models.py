from datetime import datetime, timezone

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256),  unique=True, nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(
        db.DateTime,
        index=True,
        default=datetime.now(timezone.utc).replace(tzinfo=None)
    )

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=f'http://localhost/{self.short}',
        )

    def to_dict_get_method(self):
        return dict(
            url=self.original,
        )
