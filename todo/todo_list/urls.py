from django.urls import path
from .views import (
    home,
    create_task,
    edit_task,
    remove_task,
    task_down,
    task_up,
    mark_done
)

urlpatterns = [

    path('', home, name='home'),
    path('create/', create_task, name='create_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('remove/<int:task_id>/', remove_task, name='remove_task'),
    path('down/<int:task_id>/', task_down, name='task_down'),
    path('up/<int:task_id>/', task_up, name='task_up'),
    path('done/<int:task_id>/', mark_done, name='mark_done'),
]