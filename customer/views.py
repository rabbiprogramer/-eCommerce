from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.http import JsonResponse 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, logout as singout 
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import render

from management.models import Product


def card (request):
    products = Product.objects.all()
    return render(request,'customer/card.html',{'products': products})

def Notification (request):
    return render(request,'customer/Notification.html')


def cart_view(request):
    products = Product.objects.all()
    return render(request,'customer/cart_view.html',{'products': products})

