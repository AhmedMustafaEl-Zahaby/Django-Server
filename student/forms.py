from django import forms
from .models import Student
from django.forms import ValidationError

def check_mark(value):
	if value < 0:
		raise ValidationError('Mark must be greater than 0')

def check_age(value):
	if value <= 10:
		raise ValidationError('Age must be greater than or equal to 10')

class StudentForm(forms.ModelForm):
    Age = forms.IntegerField(required=False,validators=[check_age])
    Grade = forms.IntegerField(required=False,validators=[check_mark])
    class Meta:
        model = Student
        fields = "__all__"
