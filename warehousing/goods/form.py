from django import forms
from . models import Goods


class NewGoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = "__all__"
        labels = {
            'name':"نام",
            'warehouse':"انبار مربوطه",
            'inventory':"موجودی اولیه",
        }