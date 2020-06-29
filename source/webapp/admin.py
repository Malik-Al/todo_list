from django.contrib import admin
from webapp.models import Tasks

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'created_at']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['description', 'status', 'created_at']
    readonly_fields = ['created_at']


admin.site.register(Tasks, TaskAdmin)
