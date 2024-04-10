from django.urls import path
from . import views


app_name = 'goods'
urlpatterns = [
    path('', views.GoodsView.as_view(), name='home'),   
    path('new/', views.NewGoodsView.as_view(), name='new'),   
]