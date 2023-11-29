from django.shortcuts import render
from django.shortcuts import HttpResponse,redirect
from .models import Task
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Create your views here.

def addTask(request):
    task= request.POST["task"]
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request,pk):
    task= get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed= False
    task.save()
    return redirect('home')

def edit(request,pk):
     
     enteredValue= request.POST.get('edited_task')
     get_task=get_object_or_404(Task,pk=pk)
     get_task.task=enteredValue
     get_task.save()
     return redirect('home')
        
def delete_task(request,pk):
    get_task =get_object_or_404(Task,pk=pk)
    get_task.delete()
    return redirect('home')


#how are you