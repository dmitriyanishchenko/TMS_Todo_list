from django.test import TestCase
from todo_list.models import Task


class TestTaskViews(TestCase):

    def setUp(self):
        self.task = Task(content='test')
        self.task.save()

    def test_home(self):
        result = self.client.get('')
        self.assertEqual(result.status_code, 200)

    def test_create_task(self):
        result = self.client.get('/create/')
        self.assertEqual(result.status_code, 200)

    def test_edit_task(self):
        result = self.client.get(f'/edit/{self.task.id}/')
        self.assertEquals(result.status_code, 200)

    def test_remove_task(self):
        result = self.client.get(f'/remove/{self.task.id}/')
        self.assertEquals(result.status_code, 302)
