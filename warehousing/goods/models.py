from django.db import models
from warehouse.models import Warehouse
from django.core.validators import MinValueValidator

class Goods(models.Model):
    name = models.CharField(max_length=100)
    warehouse = models.ForeignKey(
        Warehouse, related_name='goods', on_delete=models.SET_NULL, null=True
    )
    inventory = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

    def CheckInventory(self, quantity):
        if self.inventory < quantity:
            return False
        return True
    
    def UpdateInventory(self, mode, quantity):
        if mode == 'exit':
            self.inventory -= quantity
        else:
            self.inventory += quantity
        self.save()
        return True

        
