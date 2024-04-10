from django.urls import path
from . import views


app_name = 'warehouse'
urlpatterns = [
    path('', views.WarehouseView.as_view(), name='home'),
    path('new/', views.NewWarehouseView.as_view(), name='new'),
    path('detail/<int:id>/', views.DetailWarehouseView.as_view(), name='detail'),
]