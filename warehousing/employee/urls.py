from django.urls import path
from . import views

app_name = 'employee'
urlpatterns = [
    path('', views.EmployeeView.as_view(), name="home"),
    path('new/', views.NewEmployeeView.as_view(), name="new"),
]