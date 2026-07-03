from django.db import models

# Create your models here.
class Blood(models.Model):
    ID=models.IntegerField(primary_key=True)
    name=models.CharField()
    gender=models.CharField()
    age=models.IntegerField()
    phoneno=models.IntegerField()
    BGroup=models.CharField()
    state=models.CharField()
    city=models.CharField()
    password = models.CharField()
