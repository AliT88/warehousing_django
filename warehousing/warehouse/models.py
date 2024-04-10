from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} --> {self.name}'
