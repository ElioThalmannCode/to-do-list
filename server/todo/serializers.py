from rest_framework import serializers
from .models import Todo



class TodoSerializer(serializers.ModelSerializer):

    # def create(self, request, *args, **kwargs):
    #     new_todo =  Todo.objects.create(
    #         creator = self.context['request'].user,
    #         title = self.validated_data['title'],
    #         description = self.validated_data['description'],
    #         importance = self.validated_data['importance'],
    #         status = self.validated_data['status']
    #      )
    #     return new_todo

    class Meta:
        model = Todo
        fields = "__all__"