from rest_framework import serializers
from .models import Todo

from django.contrib.auth.models import User


class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=50)
    description = serializers.CharField(required=True,  max_length=500)
    creator = serializers.RelatedField(source='User', read_only=True)
    importance = serializers.IntegerField(max_value=3, min_value=1)
    status = serializers.IntegerField(max_value=3, min_value=1)

    def create(self, data):
        return Todo.objects.create(
            creator = self.context['request'].user,
            title = data['title'],
            description = data['description'],
            importance = data['importance'],
            status = data['status']
        )
    def safe(self, obj):
        return Todo.objects.create(**obj)
    def perform_create(self, serializer):
        serializer.save()