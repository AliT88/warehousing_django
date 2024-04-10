from django import forms
from .models import Warehouse


class NewWarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = "__all__"
    