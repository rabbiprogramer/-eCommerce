from django.urls import path
from .views import *
app_name = 'management'
urlpatterns = [
    path('',home, name='home'),
    path('profile/',profile,name='profile'),
    path('login',login, name='login'),
    path('card/', card, name='card'),
    path('signup/',signup,name='signup'),
    path('logout/',logout,name='logout'),
    path('add_new',add_new, name='add_new'),
    path('profile_edit/<int:id>/',profile_edit, name='profile_edit'),
    path('my_taim/',my_taim,name='my_taim'),
    path('superuser_info/', superuser_info, name='superuser_info'),
    path('add/product/',add_product,name='add_product'),
    path('all_product/',all_product,name='all_product'),
    path('profile_edit/<int:id>/',profile_edit, name='profile_edit'),
    path('product_edit/<int:id>/', product_edit, name='product_edit'),
    path('product_delete/<int:id>/', product_delete, name='product_delete'),
    path('superuser/delete/<int:id>/', superuser_delete, name='superuser_delete'),
   
]