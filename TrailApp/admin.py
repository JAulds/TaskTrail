from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'due')
    list_filter = ("status",)
    search_fields = ['title', 'content', 'due']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Task, TaskAdmin)
