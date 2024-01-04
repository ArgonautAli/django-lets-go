from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.

def home(request):
    return render(request, "homepage.html")

def todos(request):
    items = TodoItem.objects.all()
    todoList = {
        "todos": items
    }
    return render(request, "todos.html", todoList)
