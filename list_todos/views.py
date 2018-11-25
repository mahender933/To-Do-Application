from django.shortcuts import render, redirect
from .models import List
from .forms import ToDoListForm
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
            messages.success(request, ('Please enter something !!'))
        return render(request, 'list_todos/home.html', {"all_todos": all_todos})
    else:
        all_todos_list = List.objects.all()

        page = request.GET.get('page', 1)
        paginator = Paginator(all_todos_list, 10)
        try:
            all_todos = paginator.page(page)
        except PageNotAnInteger:
            all_todos = paginator.page(1)
        except EmptyPage:
            all_todos = paginator.page(paginator.num_pages)
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
    if request.method == 'POST':
        todo = List.objects.get(pk=todo_id)
        form = ToDoListForm(request.POST or None, instance=todo)
        if form.is_valid():
            form.save()
            if todo.completed:
                messages.success(request, ('You may want to uncross this task as Item has been edited !!'))  # As we are keeping the default value of `completed` set by user  and not reseting it to False by our side
            else:
                messages.success(request, ('Item has been Edited !!'))
            return redirect('home')
        else:
            messages.success(request, ('Empty value !!'))
        return render(request, 'list_todos/edit.html', {})
    else:
        todo = List.objects.get(pk=todo_id)
        return render(request, 'list_todos/edit.html', {"todo": todo})
