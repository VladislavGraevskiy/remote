from django.contrib.auth.models import User as BaseUser
from django.db import models


class Userprofile(BaseUser):
    USER_TYPE = (
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
        # ('administrator', 'Администратор'),
    )
    Courses = (
        ('1', 1), ('2', 2), ('3', 3), ('4', 4)
    )
    user_type = models.CharField('Тип пользовател', choices=USER_TYPE, max_length=20)
    student_number = models.IntegerField('Номер студенческого')
    course = models.CharField('Курс', choices=Courses, max_length=2, null=True)
    registration_approved = models.BooleanField('Регистрация одобрена?', default=False)
