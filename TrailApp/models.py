from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

TASKSTATUS = (
    (0,"Not Started"),
    (1,"In Progress"),
    (2,"Completed"),
)

class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='task_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    due = models.DateField()
    taskstatus = models.IntegerField(choices=TASKSTATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
