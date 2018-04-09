import os

# from django.conf import settings
# settings.configure()

from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "remote.settings")

application = get_wsgi_application()
from datetime import datetime, timedelta

from random import randint

from remote_control.models.models import Telemetry

some_datetime = datetime(2018, 1, 1)
for seconds in range(1, 10000000):
    date_n = some_datetime + timedelta(seconds=seconds)
    for sen_id in range(1, 23):

        Telemetry.objects.create(
            sensor_id=sen_id,
            datetime=date_n,
            value=str(randint(1, 20))
        )