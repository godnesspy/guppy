# -*- coding: utf-8 -*-

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'avril.settings')

from django.conf import settings

app = Celery('avril')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALL_APPS)