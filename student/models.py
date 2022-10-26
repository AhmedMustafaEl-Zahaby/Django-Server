from enum import unique
from operator import contains, mod
from tabnanny import check
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
class Parent(models.Model):
    Name = models.CharField(max_length = 255)

    class Meta:
        db_table = 'parent'


class Student(models.Model):
    First_name = models.CharField(max_length = 255)
    Last_name = models.CharField(max_length = 255)
    Email = models.URLField()
    Class = models.IntegerField()
    Age = models.IntegerField()
    Grade = models.IntegerField()
    parent = models.ForeignKey(Parent , related_name='student' ,on_delete=models.CASCADE)

    def clean(self):
        if self.First_name[0] < 'A' or self.First_name[0] > 'Z':
            raise ValidationError('Must start with Upper Case')

    class Meta:
        db_table = 'student'

class Subject(models.Model):
    Name = models.CharField(max_length = 255)
    student = models.ManyToManyField(Student , related_name= 'subject')

    class Meta:
        db_table = 'subject'

class Car(models.Model):
    plate_number = models.IntegerField(unique=True)
    model = models.CharField(max_length = 255)
    parent = models.OneToOneField(Parent , related_name = 'car' , on_delete = models.CASCADE)
    class Meta:
        db_table = 'car'


