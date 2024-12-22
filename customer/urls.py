from django.urls import path
from .views import *
app_name = 'customer'
urlpatterns = [
    path('',card, name='card'),
    path('cart/<int:product_id>/',cart_view, name='cart_view'),
    path('Notification',Notification, name='Notification'),


   
]
