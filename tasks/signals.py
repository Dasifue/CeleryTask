from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Task
from .tasks import mark_task

@receiver(post_save, sender=Task)
def mark_task_apply(sender, instance, **kwargs):
    mark_task.delay(instance.id)