from rest_framework import generics, permissions
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Todo

from knox.models import AuthToken

from .serializers import TodoSerializer

class TodoAPIView(viewsets.ViewSet):
    serializer_class = TodoSerializer
    permission_classes = [
            permissions.AllowAny,
        ]

    def list(self, request):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TodoSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


    
        

