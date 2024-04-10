from django import forms
from . models import Goods


class NewGoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = "__all__"