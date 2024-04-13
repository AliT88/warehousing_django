from django.shortcuts import render, redirect
from django.views import View
from . models import Employee
from . form import NewEmployeeForm
from django.contrib import messages


class EmployeeView(View):
    def get(self, request):
        em = Employee.objects.all()
        return render(request, 'employee/home.html', {'employees':em})
    

class NewEmployeeView(View):
    def get(self, request):
        form = NewEmployeeForm
        return render(request, 'employee/new.html', {'form':form})
        
    def post(self, request):
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'کارمند جدید با موفقیت ثبت گردید.', 'success')
        return redirect("employee:home")
            