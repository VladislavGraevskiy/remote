# Generated by Django 2.0.2 on 2018-03-20 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0005_auto_20180320_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.IntegerField(null=True)),
                ('send_datetime', models.DateTimeField(auto_now=True)),
                ('command', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='remote_control.Commands')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='remote_control.Userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_body', models.CharField(max_length=1000)),
                ('request', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='remote_control.Request')),
            ],
        ),
        migrations.CreateModel(
            name='UserRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]