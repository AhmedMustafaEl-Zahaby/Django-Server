from django.db import models

from parent.models import Parent
class Tokens(models.Model):
    token = models.CharField(max_length = 255)
    parent = models.ForeignKey(Parent , related_name = 'tokens' , on_delete = models.CASCADE)
    class Meta:
        db_table = 'tokens'
