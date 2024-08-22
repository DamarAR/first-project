from django.shortcuts import render, redirect
from django.http import JsonResponse   
from . models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

def add_todo(request):
    title = request.POST['title']
    description = request.POST['description']

    Todo.objects.create(title=title, description=description)
    return redirect('index')

def profile(request):
    return render(request, 'profile.html')

def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()
    return redirect('index')

def data_json(request):
    todos = Todo.objects.all()

    return JsonResponse({'data': list(todos.values())})