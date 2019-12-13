#NTSFoodCoupon/urls.py
# from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'NTSFoodCoupon'

urlpatterns = [
    url('menu', views.menu_list, name='menu_list'),
    url('token', views.token_list, name='token_list'),
    url('feedback', views.feedback, name='feedback'),
]
