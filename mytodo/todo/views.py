from django.shortcuts import render,redirect
from todo.models import Todo
from django.http import HttpResponse

# Create your views here.

def todo_list(request):
    todo = Todo.objects.order_by('-id')
    return render(request,'todo/index.html',{'todo':todo})

def create_todo(request):
    if request.method =='POST':
        title= request.POST.get('title')
        description= request.POST.get('description')
        Todo.objects.create(title=title,description=description)
        
        return redirect('todo')
    return render(request,'/')

def complete_Todo(request,id):
    # return HttpResponse('ali')
    todo = Todo.objects.get(id=id)
    todo.completed = True
    todo.save()
    return redirect('todo')

def delete_Todo(request,id):
    todo =Todo.objects.get(id=id)
    todo.delete()
    
    return redirect('todo')

def update_todo(request):
    return render(request,'update.html')
    
    

   
        
       
        
