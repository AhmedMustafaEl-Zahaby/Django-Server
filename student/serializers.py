from wsgiref.validate import validator
from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError 


def check_age(value):
    if value < 10:
        return ValidationError("Age must be greater than or equal 10")


class ParentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parent
		fields = ['Name']

class StudentSerializer(serializers.ModelSerializer):
	Age = serializers.IntegerField(validators = [check_age])
	# parent = ParentSerializer(required=False) # when getting Product: category shows name instead of id - required=False: to be able to create a product without category - did Hashem write it??
	# like forms
	class Meta:
		model = Student
		fields='__all__'

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parent
		fields = "__all__"



