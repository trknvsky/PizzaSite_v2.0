from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.task.schedules import crontab
from celery.decorators import periodic_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
app = Celery('project')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
