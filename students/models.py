from django.db import models
class student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    img=models.FileField(upload_to="imges/")


# Create your models here.
