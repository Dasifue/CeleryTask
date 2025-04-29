import time
import random
from celery import shared_task

from .models import Task

@shared_task
def mark_task(task_id):

    time.sleep(20)
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return
    
    mark = random.randint(1, 100)
    task.save(mark=mark)

