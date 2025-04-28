from django.shortcuts import render, get_object_or_404

from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {"tasks": tasks})


def get_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, "task.html", {"task": task})