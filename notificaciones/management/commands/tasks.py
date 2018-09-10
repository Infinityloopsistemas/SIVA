
from __future__ import absolute_import
from notificaciones.management.commands.notificaciones import Command
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from siva.celery import app


@periodic_task(run_every=(crontab(hour="21", minute="00", day_of_week="*")))
def inicioasyncPoll():
        tareas = Command()
        tareas.inicioPoll()

@periodic_task(run_every=(crontab(hour="23", minute="59", day_of_week="*")))
def asyncEmail():
    tareas= Command()
    tareas.envioMail()



