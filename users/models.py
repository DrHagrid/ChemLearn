from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.DO_NOTHING)
    last_reaction = models.IntegerField(verbose_name='Номер последней реакции')

    def __str__(self):
        return "%s" % self.user.username

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователях'
