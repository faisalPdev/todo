from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializer import *
from .models import *


# Create your views here.
class SampleAPIView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        return Response({"message": "Hello"})
    
class TaskListCreateAPIView(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    permission_classes=[AllowAny]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[AllowAny]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


