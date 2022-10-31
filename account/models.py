from django.db import models
from parent.models import Parent
class Account(models.Model):
    username = models.CharField(max_length = 255 , blank = False)
    password = models.CharField(max_length = 255 , blank = False)
    parent = models.OneToOneField(Parent , related_name = 'Account' , on_delete = models.CASCADE)

    class Meta:
        db_table = 'Account'


