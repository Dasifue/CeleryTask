from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Task


admin.site.unregister([User, Group])


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "mark", "timestamp"]
    list_display_links = list_display

    search_fields = ["name"]