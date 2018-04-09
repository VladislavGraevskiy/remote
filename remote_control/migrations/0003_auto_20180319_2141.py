# Generated by Django 2.0.2 on 2018-03-19 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('remote_control', '0002_auto_20180222_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('modes_of_operation', 'Режимы работы'), ('device_management', 'Управление устройствами'), ('on-board_compute', 'Бортовой компьютер')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя датчика')),
                ('category', models.CharField(choices=[('CATEGORY_ONBOARD_COMPUTER', 'Бортовой компьютер'), ('CATEGORY_TRANSCEIVER', 'Бортовой модуль связи'), ('CATEGORY_ATTITUDE', 'Бортовой модуль определения ориентации и стабилизации')], max_length=100, null=True, verbose_name='Категория')),
                ('code_name', models.CharField(max_length=100, verbose_name='Имя датчика')),
                ('unit', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Telemetry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('datetime', models.DateTimeField()),
                ('sensor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='remote_control.Sensor')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='Userprofile',
        ),
        migrations.AddField(
            model_name='commands',
            name='device',
            field=models.ManyToManyField(to='remote_control.Device'),
        ),
    ]