# Generated by Django 2.0.2 on 2018-03-29 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0006_request_response_userrequests'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='course',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4)], max_length=2, null=True, verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='commands',
            name='device',
            field=models.ManyToManyField(to='remote_control.Device'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_number',
            field=models.IntegerField(verbose_name='Номер студенческого'),
        ),
    ]
