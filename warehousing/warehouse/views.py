from django.shortcuts import render, redirect
from django.views import View
from .models import Warehouse
from .form import NewWarehouseForm
from django.contrib import messages


class WarehouseView(View):
    def get(self, request):
        wh = Warehouse.objects.all()
        return render(request, 'warehouse/home.html', {'warehouses':wh})
    

class NewWarehouseView(View):
    def get(self, request):
        form = NewWarehouseForm
        return render(request, 'warehouse/new.html', {'form':form})
    
    def post(self, request):
        form = NewWarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New warehouse created successfully.', 'success')
        return redirect('warehouse:home')


class DetailWarehouseView(View):
    def get(self, request, id):
        wh = Warehouse.objects.get(id=id)
        return render(request, 'warehouse/detail.html', {'warehouse':wh})