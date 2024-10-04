from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')  # Ensure these fields exist in Task model
