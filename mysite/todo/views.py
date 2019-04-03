from django.shortcuts import render
from .models import *


def index(request):
	todolist = TodoList.objects.all()
	context = {'TodoList' : TodoList}
	return render(request, 'Todo/index.html', context)
