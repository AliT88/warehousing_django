from django import forms
from .models import Transfer, TransferItem
from goods.models import Goods
from django_jalali import forms as jforms
from django_jalali.admin.widgets import AdminjDateWidget


class NewTransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = "__all__"
        widgets = {'date':AdminjDateWidget}
        labels = {
            'from_employee' : "تحویل دهنده",
            'to_employee' : "تحویل گیرنده",
            'mode' : "نوع",
            'date' : "تاریخ"
        }
    

class TransferItemsForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=0, label="تعداد")
    class Meta:
        model = TransferItem
        fields = ('goods', 'quantity')
        labels = {
            'goods':"کالاها",
            'quantity':"تعداد"
        }


class ReportForm(forms.Form):
    # from_date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}), label="از تاریخ")
    # to_date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}), label="تا تاریخ")
    from_date = jforms.jDateField(widget=AdminjDateWidget, label="از تاریخ")
    to_date = jforms.jDateField(widget=AdminjDateWidget, label="تا تاریخ")

    selection_choices = (
        ( None, ''),
        ('exit', 'خروج'),
        ('entry', 'ورود'),
    )
    mode = forms.ChoiceField(choices=selection_choices, label="نوع")

    selection_goods = [(None,'')]
    for item in Goods.objects.values('name').all():
        selection_goods.append((str(item['name']), str(item['name'])))
    selection_goods = tuple(selection_goods)
    goods = forms.ChoiceField(choices=selection_goods, label="کالا")
    