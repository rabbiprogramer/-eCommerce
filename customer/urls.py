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
    path('product/<int:id>/',product_detail, name='product_detail'),
    path('order/detail/<int:id>/',order_detail, name='order_detail'),
    path('order/delete/<int:id>/',delete_order, name='delete_order'),
    path('massage',massage, name='massage'),
    path('login',login, name='login'),
    path('sign_in',sign_in, name='sign_in'),
    
]


   
