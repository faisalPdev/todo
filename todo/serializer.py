from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Task
        fields = '__all__'