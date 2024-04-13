from django.db import models
from goods.models import Goods
from employee.models import Employee
from django.core.validators import MinValueValidator
from django_jalali.db import models as jmodels

class Transfer(models.Model):
    choices = [
        ('entry', 'ورود'),
        ('exit', 'خروج')
    ]
    mode = models.CharField(max_length=10, choices=choices)
    from_employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL,
        related_name='transfers_from', null=True
        )
    to_employee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, 
        related_name='transfers_to', null=True
        )
    date = jmodels.jDateField()

    class Meta:
        ordering = ('-date',)


class TransferItem(models.Model):
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE, related_name='items')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0),])