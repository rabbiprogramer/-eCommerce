from django.urls import path
from .views import *
app_name = 'customer'
urlpatterns = [
    path('',card, name='card'),
    path('cart/<int:product_id>/',cart_view, name='cart_view'),
    path('order',order, name='order'),
    path('Notification',Notification, name='Notification'),
    path('customer_home',customer_home, name='customer_home'),
    path('process_to_checkout',process_to_checkout, name='process_to_checkout'),
    path('product/<int:product_id>/detail/', product_detail, name='product_detail'),


   
]
