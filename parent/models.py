from lib2to3.pgen2 import token
from django.db import models
class Parent(models.Model):
    name = models.CharField(max_length = 255)
    class Meta:
        db_table = 'parent'
    def __str__(self):
        return self.name
        



