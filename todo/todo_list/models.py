from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=300)
    completed = models.BooleanField(default=False)
    priority = models.TextField(default='low')

    def update_id(self, value):
        Task.objects.filter(id=self.id).update(id=value)

    def __str__(self):
        return f' {self.content}'
# Create your models here.
