from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from todo_list.models import Task
from todo_list.forms import TaskForm


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'GET':
        context = {'form': TaskForm(initial={'content': task.content})}
        return render(request, 'edit_task.html', context)
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Task.objects.filter(id=task_id).update(**data)
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(errors)
    else:
        return HttpResponse('INVALID REQUEST')
