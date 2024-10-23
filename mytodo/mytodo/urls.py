
from django.contrib import admin
from django.urls import path
from todo.views import todo_list,create_todo,complete_Todo,delete_Todo,update_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todo_list, name="todo"),
    path('create/',create_todo, name="create_todo"),
    path('complete/<int:id>',complete_Todo, name="complete_Todo"),
    path('delete/<int:id>',delete_Todo, name="delete_Todo"),
    path('update/<int:id>',update_todo,  name="update_todo")
]
