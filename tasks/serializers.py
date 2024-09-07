from rest_framework import serializers
from tasks.models import Task


# serializers.ModelSerializer автоматически предоставляет эти методы на основе модели(методы CRUD)
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'