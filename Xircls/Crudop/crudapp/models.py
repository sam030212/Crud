from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    Address = models.TextField(max_length=100)
    phone = models.IntegerField(max_length=20)

    def __str__(self):
        return self.name
