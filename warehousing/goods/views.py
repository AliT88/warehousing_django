from django.shortcuts import render, redirect
from django.views import View
from .models import Goods
from .form import NewGoodsForm
from django.contrib import messages


class GoodsView(View):
    def get(self, request):
        gd = Goods.objects.all()
        return render(request, 'goods/home.html', {'goods':gd})


class NewGoodsView(View):
    def get(self, request):
        form = NewGoodsForm
        return render(request, 'goods/new.html', {'form':form})
    
    def post(self, request):
        form = NewGoodsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New goods created successfully.')
        return redirect('goods:home')



