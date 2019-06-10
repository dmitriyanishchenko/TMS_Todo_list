from django.urls import path
from .views import (
    home,
    create_task,
    edit_task,
    remove_task,
)

urlpatterns = [

    path('', home, name='home'),
    path('create/', create_task, name='create_task'),
    path('edit/<int:task_id>/', edit_task, name='edit_task'),
    path('remove/<int:task_id>/', remove_task, name='remove_task'),
]