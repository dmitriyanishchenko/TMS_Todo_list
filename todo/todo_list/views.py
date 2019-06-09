from django.shortcuts import render
from .models import Task


def home(request):
    task = Task.objects.all()
    context = {'task': task}
    return render(request, 'home_task.html', context)

# Create your views here.
