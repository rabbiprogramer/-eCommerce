from django.urls import path
from .views import *
app_name = 'management'
urlpatterns = [
    path('',home, name='home'),
    path('profile/',profile,name='profile'),
    path('login/',login, name='login'),
    path('signup/',signup,name='signup'),
    path('logout/',logout,name='logout'),
    path('add_new',add_new, name='add_new'),
    path('profile_edit/<int:id>/',profile_edit, name='profile_edit'),
    path('my_taim/',my_taim,name='my_taim'),
    path('superuser_info/', superuser_info, name='superuser_info'),
   
]