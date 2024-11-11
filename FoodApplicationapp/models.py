from django.db import models

# Create your models here.

class Restarent(models.Model):
    restarentId=models.IntegerField(primary_key=True)
    restarentName=models.CharField(max_length=15)
    restarentLocation=models.CharField(max_length=15)


class Food(models.Model):
    foodId=models.IntegerField(primary_key=True)
    foodName=models.CharField(max_length=15)
    foodPrice=models.IntegerField()