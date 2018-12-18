from rest_framework import serializers
from classes.models import Classroom

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject','year','teacher']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        exclude = ['teacher']

