from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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
            last_id = Task.objects.last().id if Task.objects.last() else 1
            currently_created_task = Task.objects.last()
            currently_created_task.update_id(last_id + 1)
            return redirect('home')
        else:
            errors = form.errors
            return HttpResponse(f'{errors}')
    return HttpResponse('Wrong request method')


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


def remove_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    for new_id, task in enumerate(Task.objects.all(), start=1):
        task.update_id(new_id)
    return redirect('home')


def task_down(request, task_id):
    if not task_id == Task.objects.last().id:
        task_we_want_to_lower_down = get_object_or_404(Task, id=task_id)
        task_lift_up = Task.objects.get(id=task_id + 1)
        task_lift_up.id, task_we_want_to_lower_down.id = task_we_want_to_lower_down.id, task_lift_up.id
        task_we_want_to_lower_down.save()
        task_lift_up.save()
        return redirect('home')
    return redirect('home')


def task_up(request, task_id):
    if not task_id == Task.objects.first().id:
        task_we_want_to_rise = get_object_or_404(Task, id=task_id)
        task_lower_down = Task.objects.get(id=task_id - 1)
        task_we_want_to_rise.id, task_lower_down.id = task_lower_down.id, task_we_want_to_rise.id
        task_we_want_to_rise.save()
        task_lower_down.save()
        return redirect('home')
    return redirect('home')
