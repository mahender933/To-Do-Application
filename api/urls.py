from django.urls import path
from . import views

urlpatterns = [
    path('', views.ToDoList.as_view(), name='api-todo-list'),
]
