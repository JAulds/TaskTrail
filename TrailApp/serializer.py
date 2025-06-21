from rest_framework import serializers

from TrailApp.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'content', 'status', 'author']
