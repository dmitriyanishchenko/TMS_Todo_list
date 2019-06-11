from django.shortcuts import redirect, get_object_or_404
from todo_list.models import Task


def mark_completed(request, task_id):
    task_we_completed = get_object_or_404(Task, id=task_id)
    task_we_completed.completed = True if not task_we_completed.completed else False
    task_we_completed.save()
    return redirect('home')
