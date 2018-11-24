from django.shortcuts import render, redirect
from .models import List
from .forms import ToDoListForm
from django.contrib import messages
from django.utils import timezone


def home(request):
    if request.method == 'POST':
        form = ToDoListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_todos = List.objects.all()
            messages.success(request, ('Item added to the list !!'))
            return render(request, 'list_todos/home.html', {"all_todos": all_todos})
    else:
        all_todos = List.objects.all()
        return render(request, 'list_todos/home.html', {"all_todos": all_todos})


def about(request):
    return render(request, 'list_todos/about.html', {})


def delete(request, todo_id):
    try:
        item = List.objects.get(pk=todo_id)
        item.delete()
        messages.success(request, ('Item has been successfully deleted !!'))
    except List.DoesNotExist:
        messages.success(request, ('Item already does not exists !!'))
    return redirect('home')


def change_status(request, todo_id):
    item = List.objects.get(pk=todo_id)
    if item.completed:
        item.completed = False
        item.updated_at = timezone.now()
        item.save()
    else:
        item.completed = True
        item.updated_at = timezone.now()
        item.save()
    return redirect('home')


def edit_todo(request, todo_id):
    pass
