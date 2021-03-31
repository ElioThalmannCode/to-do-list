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
        queryset = Todo.objects.filter(creator=request.user)
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = TodoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def destroy(self,request,pk):
        print(pk)
        instance = Todo.objects.get(id=pk)
        self.perform_destroy(instance)
        return Response(status=201)

    def perform_destroy(self, instance):
        instance.delete()
    
        

