from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post, Task
from .serializers import PostSerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet

@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        print("Incoming data (create):", request.data)  
        response = super().create(request, *args, **kwargs)
        print("Saved instance (create):", self.get_object())  
        return response

    def update(self, request, *args, **kwargs):
        print("Incoming data (update):", request.data) 
        response = super().update(request, *args, **kwargs)
        print("Saved instance (update):", self.get_object())  # Debug statement
        return response