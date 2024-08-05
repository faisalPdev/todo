from django.urls import path
from .views import *


urlpatterns = [
    path('hello/', SampleAPIView.as_view()),
    path('task/', TaskListCreateAPIView.as_view()),
    path('task/detail/<int:pk>/', TaskDetailAPIView.as_view()),
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/detail/<int:pk>/', TaskDetailAPIView.as_view()),
    
]