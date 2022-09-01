from django.db import models

class Service(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=20)
    roll=models.CharField(max_length=30)
    reg=models.CharField(max_length=30)