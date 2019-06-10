from django.urls import path
from .views import home, create_task

urlpatterns = [

    path('', home, name='home'),
    path('create/', create_task, name='create_task'),
]