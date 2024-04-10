from django import forms
from .models import Transfer, TransferItem
from django.contrib.admin.widgets import AdminDateWidget


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
