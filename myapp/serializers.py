from rest_framework import serializers
from .models import Post, Task

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'priority', 'deadline', 'comments']

    def validate_deadline(self, value):
        print("Validating deadline:", value)
        return value
