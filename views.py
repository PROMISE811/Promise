from django.shortcuts import render
from rest_framework import generics
from .models import ToDo 
from .serializers import *
from .models import *
#CRUD Operation
class ListTodo(generics.ListAPIView):
    serializer_class = ToDoSerializer

    def get_queryset(self):
        # Optionally, you can filter or modify the queryset here
        return Todo.objects.all()
    
class DetailTodo(generics.RetrieveUpdateAPIView):  #Update
    Queryset = ToDo.objects.all()   
    serializer_class = ToDoSerializer
    
class CreateTodo(generics.CreateAPIView):    #Create
    Queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class DeleteTodo(generics.DestroyAPIView):  #Delete
    Queryset = ToDo.objects.all()   
    serializer_class = ToDoSerializer