from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

@shared_task(name='subtraction task')
def sub(x, y):
    sleep(10)
    return x - y

# @shared_task
# def clear_session_cache(id):
#     print(f"Session Cache Cleared {id}")
#     return id

@shared_task(name = 'clear_session_cache_task')
def clear_session_cache(id):
    print(f"Session Cache Cleared {id}")
    return id


@shared_task
def clear_redis_data(key):
    print(f"Redis Data Cleared {key}")
    return key

@shared_task
def clear_rabbitMQ_data(key):
    print(f"Redis Data Cleared {key}")
    return key

# Create a schedule for every 30sec
schedule, _ = IntervalSchedule.objects.get_or_create(
    every = 30,
    period = IntervalSchedule.SECONDS,
)

# Schedule perodic task
PeriodicTask.objects.get_or_create(
    name = 'Clear rabbitMQ data',
    task = 'myapp.tasks.clear_rabbitMQ_data',
    interval = schedule,
    args = json.dumps(['hello from vs code']),
)

