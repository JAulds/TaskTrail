from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

# Create your tests here.

class TaskStatusUpdateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Test Task',
            slug='test-task',
            author=self.user,
            content='Some content',
            due='2025-06-10',
            status=1,
            taskstatus=0  # Not Started
        )

    def test_taskstatus_update(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('update_task_status', args=[self.task.pk]), {
            'taskstatus': 2  # Completed
        })

        self.task.refresh_from_db()
        self.assertEqual(self.task.taskstatus, 2)
        self.assertEqual(response.status_code, 302)  # Expect redirect after POST

class TaskAccessControlTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Unauthorized Access Test',
            slug='unauthorized-task',
            author=self.user,
            content='Secure content',
            due='2025-06-15',
            status=1,
            taskstatus=0
        )

    def test_update_task_requires_login(self):
        response = self.client.get(reverse('update_task_status', args=[self.task.pk]))
        # Should redirect to login
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.url)
