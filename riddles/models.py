from django.db import models

# Create your models here.

class Student(models.Model):
    Full_Name = models.CharField(max_length=50)
    Faculty = models.CharField(max_length=30)
    Group = models.CharField(max_length=30)
    Course = models.IntegerField()
    Date = models.CharField(max_length=10)
    Reason = models.CharField(max_length=255)
    

    