from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def home(request):
    task = Task.objects.all()
    context = {'task': task}
    return render(request, 'home_task.html', context)


def create_task(request):
    if request.method == 'GET':
        context = {'form': TaskForm()}
        return render(request, 'create_task.html', context)
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Task.objects.create(**data)

            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')
