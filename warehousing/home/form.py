from django import forms
from .models import Transfer, TransferItem
from goods.models import Goods


class NewTransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = "__all__"
        widgets = {'date':forms.NumberInput(attrs={'type':'date'})}
    

class TransferItemsForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=0)
    class Meta:
        model = TransferItem
        fields = ('goods', 'quantity')


class ReportForm(forms.Form):
    from_date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    to_date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    
    selection_choices = (
        ( None, ''),
        ('exit', 'Exit'),
        ('entry', 'Entry'),
    )
    mode = forms.ChoiceField(choices=selection_choices)

    selection_goods = [(None,'')]
    for item in Goods.objects.values('name').all():
        selection_goods.append((str(item['name']), str(item['name'])))
    selection_goods = tuple(selection_goods)
    goods = forms.ChoiceField(choices=selection_goods)
    