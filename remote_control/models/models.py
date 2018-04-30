from datetime import timedelta

from django.contrib.postgres.forms import RangeWidget
from django.db import models
import django_filters
from django_filters.widgets import RangeWidget
from django_filters.filters import ChoiceFilter, DateTimeFromToRangeFilter


from remote_control.models.user import Userprofile


SENSOR_CATEGORY = (
    ('CATEGORY_ONBOARD_COMPUTER', 'Бортовой компьютер'),
    ('CATEGORY_TRANSCEIVER', 'Бортовой модуль связи'),
    ('CATEGORY_ATTITUDE', 'Бортовой модуль определения \n ориентации и стабилизации'),
)


class Sensor(models.Model):
    name = models.CharField('Имя датчика', max_length=100)
    category = models.CharField('Категория', max_length=100, choices=SENSOR_CATEGORY, null=True, blank=True)
    code_name = models.CharField('Имя датчика', max_length=100)
    unit = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'

    def __str__(self):
        return self.name

    @staticmethod
    def get_sensors_name():
        return Sensor.objects.all().values_list('code_name', 'name')


class Telemetry(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    datetime = models.DateTimeField()

    class Meta:
        verbose_name = 'Телеметрия'
        verbose_name_plural = 'Телеметрия'

    def __str__(self):
        return self.value


class TelemetryFilter(django_filters.FilterSet):
    datetime = DateTimeFromToRangeFilter()
    sensor__category = ChoiceFilter(choices=SENSOR_CATEGORY)
    sensor__code_name = ChoiceFilter(choices=Sensor.get_sensors_name())

    class Meta:
        model = Telemetry
        fields = ['datetime', 'sensor__category', 'sensor__code_name']
    # sensor = django_filters.
    # sensor__category = ChoiceFilter(choices=SENSOR_CATEGORY)
    # fields = {'datetime': ['lt', 'gt']
    #           }


COMMANDS_CATEGORY = (
    ('modes_of_operation', 'Режимы работы'),
    ('device_management', 'Управление устройствами'),
    ('on-board_compute', 'Бортовой компьютер'),
)


class Device(models.Model):
    name = models.CharField(max_length=100)

SYSTEM = (
    ('0', 'основная'),
    ('1', 'резервная'),
)


class Commands(models.Model):
    command = models.CharField(max_length=100)
    name = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, choices=COMMANDS_CATEGORY)
    enable_device = models.BooleanField(default=False)
    enable_argument = models.BooleanField(default=False)
    system = models.CharField(max_length=20, choices=SYSTEM,  null=True, blank=True)
    trust_level = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Комманда'
        verbose_name_plural = 'Комманды'

    def __str__(self):
        return self.name

    @staticmethod
    def get_command_name():
        return Commands.objects.all().values_list('command', 'name')


class Request(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.DO_NOTHING)
    command = models.ForeignKey(Commands, on_delete=models.DO_NOTHING)
    cid = models.CharField(max_length=100, null=True)
    send_datetime = models.DateTimeField(auto_now=True)
    device = models.CharField(max_length=20, null=True, blank=True)
    argument = models.CharField(max_length=20, null=True, blank=True)
    time_of_execution = models.DateTimeField(null=True, blank=True)

    def get_request_data(self):
        dict_params = {
            'время': self.send_datetime.strftime('%H:%M:%S %Y-%m-%d'),
            'комманда': self.command.name,
            'cid': self.cid
        }
        if self.argument:
            dict_params['аргумент'] = self.argument
        if self.device:
            dict_params['устройство'] = self.device

        return dict_params


class Response(models.Model):
    request = models.OneToOneField(Request, null=True, on_delete=models.DO_NOTHING)
    response_body = models.CharField(max_length=1000)


class Schedule(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.DO_NOTHING)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class SessionRequests(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING)
    request = models.ManyToManyField(Request)


class RawData(models.Model):
    response_datetime = models.DateTimeField(auto_now=True)
    raw_data = models.CharField(max_length=5000)




