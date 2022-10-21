from unicodedata import name
from django.db import models

class Student(models.Model):
    First_name = models.CharField(max_length = 255)
    Second_name = models.CharField(max_length = 255)
    Email = models.URLField(max_length = 200)
    Class = models.IntegerField()
    Age = models.IntegerField()
    def __str__(self): 
        return self.name	

class Meta:
	db_table = 'students'