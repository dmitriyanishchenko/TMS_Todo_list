from django.shortcuts import render
from todo_list.models import Task


def home(request):
    task = Task.objects.all()
    context = {'task': task}
    return render(request, 'home_task.html', context)
