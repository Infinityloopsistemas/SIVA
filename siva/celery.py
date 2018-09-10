from __future__ import absolute_import
import os
from celery import Celery
from siva import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','siva.settings')

app = Celery('siva.givasl.com',
             broker='amqp://',
             backend='amqp://')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

class Config:
    CELERY_ENABLE_UTC = True
    CELERY_TIMEZONE = 'Atlantic/Canary'

app.config_from_object(Config)


# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()