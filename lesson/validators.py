from rest_framework.exceptions import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        url = dict(value).get(self.field)
        if 'youtube.com' not in url:
            raise ValidationError('Материалы не должны содержать ссылку на сторонние ресурсы, кроме youtube.com.')
