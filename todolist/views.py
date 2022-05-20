from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST) 
        if form.is_valid():
            form.save() 
        return redirect('/todolist')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todolist/index.html', context)

def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    context = {'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) 
        if form.is_valid():
            form.save() 
        return redirect('/todolist')
    return render(request, 'todolist/update_task.html', context)

def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}

    if request.method == 'POST':
        item.delete()
        return redirect('/todolist')
    return render(request, 'todolist/delete_task.html', context)