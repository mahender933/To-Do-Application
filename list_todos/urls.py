from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<todo_id>', views.delete, name='delete'),
    path('change-status/<todo_id>', views.change_status, name='change_status'),
    path('edit/<todo_id>', views.edit_todo, name='edit'),
]
