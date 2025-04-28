from django.db import models

class Task(models.Model):

    name = models.CharField(max_length=1024)
    description = models.TextField(null=True, blank=True)
    mark = models.PositiveSmallIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
