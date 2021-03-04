from rest_framework import serializers
from .models import *

class Movie_details_serializer(serializers.Serializer):
    class Meta:
        model = Movie_details_model
        fields = '__all__'

class Vote_system_serializer(serializers.Serializer):
    class Meta:
        model = Vote_system_model
        fields = '__all__'