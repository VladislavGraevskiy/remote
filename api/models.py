from functools import partial

from django.db import models

from api.utils import get_random_string

get_random_token = partial(get_random_string, size=16)


class APIToken(models.Model):

    token = models.CharField(max_length=16, unique=True, default=get_random_token)
    # по умолчанию токен бессмертный
    expires = models.PositiveIntegerField(null=True)
    # просто коментарий, чтобы написать, чей токен
    comment = models.CharField(max_length=128, null=True)
    # список обработчиков через запятую, к которым токену разрешен доступ
    handlers = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'

    @classmethod
    def create_token(cls, comment, handlers):
        return cls.objects.create(comment=comment, handlers=','.join(handlers))

    def get_handlers(self):
        return self.handlers.split(',')
