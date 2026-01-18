import os
import time
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(name='Addition task')
def add(x, y):
    time.sleep(5)
    return x + y

# Method 2
# app.conf.beat_schedule = {
#     'every-10-seconds': {
#         'task': 'clear_session_cache_task',
#         'schedule': 10,
#         'args': ('from celery',)
#     },
# }

# Using crontab
# app.conf.beat_schedule = {
#     'every-10-seconds': {
#         'task': 'clear_session_cache_task',
#         'schedule': crontab(hour=13, minute=43), #Time 13:43 or 01:13PM (Everyday)
#         'args': ('from celery',)
#     },
# }


# Using timedelta
app.conf.beat_schedule = {
    'every-10-seconds': {
        'task': 'clear_session_cache_task',
        'schedule': timedelta(minutes=1),
        'args': ('from celery',)
    },
}