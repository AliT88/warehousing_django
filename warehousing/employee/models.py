from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name

