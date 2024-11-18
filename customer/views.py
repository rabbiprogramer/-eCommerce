from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.http import JsonResponse 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, logout as singout 
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import *



def base(request):

    return render(request, 'base.html',)

