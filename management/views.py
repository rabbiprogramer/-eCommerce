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
from .forms import CustomSuperuserForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import *



def home(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'management/home.html', {'profile': profile})

def add_new(request):
    if request.method == 'POST':
        form = CustomSuperuserForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the superuser
            messages.success(request, "Superuser created successfully!")  # Success message
            return redirect('management:home')  # Redirect to home page after successful form save
    else:
        form = CustomSuperuserForm()

    return render(request, 'management/add_new.html', {'form': form})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_product') 
        else:
            print(form.errors)  
    else:
        form = ProductForm()
        print(request.POST)
        print(request)
        
    return render(request, 'management/add_product.html', {'form': form})


def all_product(request):
    products = Product.objects.all()
    return render(request, 'management/all_product.html', {'products': products})


@login_required(login_url="/management/login")
def management(request):
    return render(request,'management.html')

@login_required(login_url="/management/login")
def home (request):
    return render(request,'management/home.html')

# @login_required(login_url="/account/login")
def profile(request):
    # Query all users (or filter based on your logic)
    all_profiles = User.objects.all()

    context = {
        "all_profiles": all_profiles,  # Use a queryset, not the model class
    }

    return render(request, 'management/profile.html', context)

#@login_required(login_url="/account/login")
def login(request):
    message = None
    if request.method == 'POST':   
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user) 
                return redirect('management:home')
            else:
                message = "Invalid credentials"
        else:
            message = "Username and Password are required"
    
    context = {
        "message": message
    }

    return render(request,'management/login.html', context)

def signup(request): 
    massage = None 
    if request.method == 'POST': 
        username = request.POST.get('username') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
 
        if username and email and password: 
            user = User.objects.create_user( 
                username=username, 
                email=email,
                password=password ,
            ) 
            user.save() 
            login(request, user)
            return redirect('management:home') 
        else: 
            massage = "username and password is requard" 
 
    context = { 
        'massage' : massage 
    } 
 
    return render(request, 'management/signup.html', context) 

def logout(request): 
    singout(request) 
    return redirect('management:login')






def my_taim(request):

    return render (request,'management/my_taim.html')

@login_required



def profile_edit(request, id):
    try:
        profile = Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        raise Http404(f"Profile does not exist with id: {id}")

    if request.method == 'POST':
        fathers_name = request.POST.get('fathers_name')
        mothers_name = request.POST.get('mothers_name')
        profile_image = request.FILES.get('profile_image')  # Use request.FILES for file uploads
        address = request.POST.get('address')
        blood_group = request.POST.get('blood_group')
        email = request.POST.get('email')

        
        profile.fathers_name = fathers_name
        profile.mothers_name = mothers_name
        profile.profile_image = profile_image
        profile.address = address
        profile.blood_group = blood_group
        profile.email = email

       
        profile.save()
        messages.success(request, 'Your profile has been successfully updated!')                       
        return redirect("management:profile")
    context = {
        'profile': profile,
    }

    return render(request, 'management/profile_edit.html', context)


def superuser_info(request):
    if not request.user.is_authenticated:  
        return redirect('login')
    if not request.user.is_superuser:  
        return redirect('home')  
    superusers = User.objects.filter(is_superuser=True)
    context = {
        'superusers': superusers,
        'superuser_count': superusers.count(),
    }
    return render(request, 'management/superuser_info.html', context)



def product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('management:all_product') # Redirect to product list after editing
    else:
        form = ProductForm(instance=product)
    return render(request, 'management/product_edit.html', {'form': form})

def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
   
    return redirect('management:all_product')