from django.db import models

class Service(models.Model):
    name=models.CharField(max_length=130)
    email=models.CharField(max_length=150)
    roll=models.CharField(max_length=130)
    reg=models.CharField(max_length=130)