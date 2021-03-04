from rest_framework import serializers
from .models import Todo_list

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo_list
        fields = '__all__'