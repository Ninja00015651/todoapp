import pytest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task, Category, Comment


@pytest.mark.django_db
class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.category = Category.objects.create(name='Work', created_by=self.user)
        self.task = Task.objects.create(
            title='Test Task',
            description='Test description',
            owner=self.user,
            priority='high',
            status='pending'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.owner, self.user)
        self.assertEqual(self.task.status, 'pending')

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Work')
        self.assertEqual(self.category.created_by, self.user)

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Work')

    def test_comment_creation(self):
        comment = Comment.objects.create(task=self.task, author=self.user, body='Nice task!')
        self.assertEqual(comment.body, 'Nice task!')
        self.assertEqual(comment.task, self.task)


@pytest.mark.django_db
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.task = Task.objects.create(
            title='Test Task',
            owner=self.user,
            status='pending',
            priority='medium'
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_task_list_requires_login(self):
        response = self.client.get(reverse('task_list'))
        self.assertRedirects(response, '/accounts/login/?next=/tasks/')

    def test_task_list_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)

    def test_task_detail_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('task_detail', kwargs={'pk': self.task.pk}))
        self.assertEqual(response.status_code, 200)

    def test_task_create(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('task_create'), {
            'title': 'New Task',
            'description': 'Description',
            'priority': 'low',
            'status': 'pending',
        })
        self.assertEqual(Task.objects.filter(title='New Task').count(), 1)

    def test_task_update(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('task_update', kwargs={'pk': self.task.pk}), {
            'title': 'Updated Task',
            'priority': 'high',
            'status': 'done',
        })
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_task_delete(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(reverse('task_delete', kwargs={'pk': self.task.pk}))
        self.assertEqual(Task.objects.filter(pk=self.task.pk).count(), 0)
