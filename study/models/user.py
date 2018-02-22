from django.contrib.auth.models import User as BaseUser
from django.db import models


class Userprofile(BaseUser):
    USER_TYPE = (
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
        ('administrator', 'Администратор'),
    )
    user_type = models.CharField('Тип пользовател', choices=USER_TYPE)
    student_number = models.IntegerField('Номер студенческого')

    class Meta:
        app_label = 'study'

