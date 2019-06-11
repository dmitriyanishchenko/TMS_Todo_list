from django.http import HttpResponse
from django.shortcuts import render, redirect
from todo_list.models import Task
from todo_list.forms import TaskForm


def create_task(request):
    if request.method == 'GET':
        context = {'form': TaskForm()}
        return render(request, 'create_task.html', context)
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Task.objects.create(**data)
            last_id = Task.objects.last().id if Task.objects.last() else 1
            currently_created_task = Task.objects.last()
            currently_created_task.update_id(last_id + 1)
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')