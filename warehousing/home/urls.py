from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.TransferView.as_view(), name='home'),
    path('new/', views.NewTransferView.as_view(), name='new'),
    path('detail/<int:id>/', views.DetailTransferView.as_view(), name='detail'),
    path('addgoods/', views.AddGoodsToTransferView.as_view(), name='add_goods'),
    path('remove/<int:id>', views.RemoveView.as_view(), name='remove'),
]