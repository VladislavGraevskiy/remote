import os

# from django.conf import settings
# settings.configure()

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "remote.settings")

application = get_wsgi_application()
from remote_control.models.models import Sensor

k = [{
  "version": "0.1",
  "name": "Панель отображения телеметрии",
  "categories":
  [
    {
      "name": "Бортовой компьютер",
      "category": "CATEGORY_ONBOARD_COMPUTER",
      "columns": 1,
      "sensors":
      [
        {
          "name": "Активная система",
          "sensor": "onboard_number",
          "unit": ""
        },
        {
          "name": "Загруженность ЦП",
          "sensor": "onboard_cpu",
          "unit": "%"
        },
        {
          "name": "Загруженность ОЗУ",
          "sensor": "onboard_ram",
          "unit": "%"
        },
        {
          "name": "Температура ЦП",
          "sensor": "onboard_temp",
          "unit": "℃"
        }
      ]
    },
    {
      "name": "Бортовой модуль связи",
      "category": "CATEGORY_TRANSCEIVER",
      "columns": 1,
      "sensors":
      [
        {
          "name": "Несущая частота",
          "sensor": "transceiver_frequency",
          "unit": "МГц"
        },
        {
          "name": "Скорость передачи",
          "sensor": "transceiver_speed",
          "unit": "кБ/с"
        },
        {
          "name": "Активный передатчик",
          "sensor": "transceiver_active",
          "unit": ""
        },
        {
          "name": "Время приема пакета",
          "sensor": "transceiver_timestamp",
          "unit": ""
        },
        {
          "name": "Размер пакета",
          "sensor": "transceiver_length",
          "unit": "байт"
        }
      ]
    },
    {
      "name": "Бортовой модуль определения ориентации и стабилизации",
      "category": "CATEGORY_ATTITUDE",
      "columns": 2,
      "sensors":
      [
        {
          "name": "Солнечный датчик №1",
          "sensor": "attitude_light_1",
          "unit": "усл.ед."
        },
        {
          "name": "Солнечный датчик №2",
          "sensor": "attitude_light_2",
          "unit": "усл.ед."
        },
        {
          "name": "Солнечный датчик №3",
          "sensor": "attitude_light_3",
          "unit": "усл.ед."
        },
        {
          "name": "Солнечный датчик №4",
          "sensor": "attitude_light_4",
          "unit": "усл.ед."
        },

        {
          "name": "Акселерометр, X",
          "sensor": "attitude_accel_x",
          "unit": "м/с²"
        },
        {
          "name": "Акселерометр, Y",
          "sensor": "attitude_accel_y",
          "unit": "м/с²"
        },
        {
          "name": "Акселерометр, Z",
          "sensor": "attitude_accel_z",
          "unit": "м/с²"
        },

        {
          "name": "Магнетометр, X",
          "sensor": "attitude_magn_x",
          "unit": "мГс"
        },
        {
          "name": "Магнетометр, Y",
          "sensor": "attitude_magn_y",
          "unit": "мГс"
        },
        {
          "name": "Магнетометр, Z",
          "sensor": "attitude_magn_z",
          "unit": "мГс"
        },

        {
          "name": "Гироскоп, X",
          "sensor": "attitude_gyro_x",
          "unit": "Град/с"
        },
        {
          "name": "Гироскоп, Y",
          "sensor": "attitude_gyro_y",
          "unit": "Град/с"
        },
        {
          "name": "Гироскоп, Z",
          "sensor": "attitude_gyro_z",
          "unit": "Град/с"
        },

        {
          "name": "Температура платы",
          "sensor": "attitude_temp",
          "unit": "℃"
        }
      ]
    }
  ]}]


for i in k[0]['categories']:
  cat = i['category']
  for ij in i['sensors']:
    Sensor.objects.create(
      name=ij['name'],
      code_name=ij['sensor'],
      category=cat,
      unit=ij['unit']
    )
    print(ij, cat)



