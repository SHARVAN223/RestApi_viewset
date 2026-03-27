from rest_framework import serializers
from app.models import *
class Stu_serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    