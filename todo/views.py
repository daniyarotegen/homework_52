from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from todo.models import Task


def index_view(request: WSGIRequest):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'task_create.html', {'task': Task()})
    task_data = {
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'completion_date': request.POST.get('completion_date')
    }
    Task.objects.create(**task_data)
    return redirect('/')
