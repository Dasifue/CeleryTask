import time
import random
from celery import shared_task

from .models import Task

@shared_task
def mark_task(task_id):
    time.sleep(5) # анализ оценки с помощью ИИ
    Task.objects.filter(id=task_id).update(mark=random.randint(1, 100))

