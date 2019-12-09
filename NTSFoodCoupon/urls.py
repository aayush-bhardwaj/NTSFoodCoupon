#NTSFoodCoupon/urls.py
# from django.urls import path
from . import views
from django.conf.urls import url
app_name = 'NTSFoodCoupon'
urlpatterns = [
    url('menu', views.menu_list, name='menu_list'),
]