from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.http import JsonResponse 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, logout as singout 
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ValidationError

from .models import *
from management.models import Product


def card (request):
    products = Product.objects.all()
    return render(request,'customer/card.html',{'products': products})

def Notification (request):
    return render(request,'customer/Notification.html')




def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})







def customer_home(reqeust):

    products = Product.objects.all()
    query = reqeust.GET.get('search', '')
    
    if query:
        # Filter products where the name contains the search query (case insensitive)
        products = products.filter(name__icontains=query)

    paginator = Paginator(products, 1)      
    page_number = reqeust.GET.get('page')
    try:
        paginated_products = paginator.page(page_number)

    except PageNotAnInteger:
        paginated_products = paginator.page(1)

    except EmptyPage: 
        paginated_products = paginator.page(paginator.num_pages)
    context = {
        'products':products,
        # 'paginated_products': paginated_products,
        'query': query,
       
    }

    if reqeust.headers.get('HX-Request'):
        return render(reqeust, 'customer/search_results.html', context)


    return render(reqeust, 'customer/customer_home.html', context)

def delete_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)  
    cart_item.delete()  
    return redirect('/') 

def add_card(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:  
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('/') 

def cart_view(request):

    product = Product.objects.all()
    cart = get_object_or_404(Cart, user=request.user, is_active=True)
    cart_items = CartItem.objects.filter(cart=cart)
    carts = Cart.objects.filter(user=request.user, is_active=True)
    total_price_of_all_carts = sum(cart.total_price() for cart in carts)
    total_price = cart.total_price()  

    return render(request, 'customer/cart_view.html', {'cart_items': cart_items, 'total_price': total_price, 'total_price_of_all_carts': total_price_of_all_carts, 'product': product})

# def send_checkout_notifications(user, final_total_price):
    
#     message_for_customer = f"Hello {user.username}, your order total is ${final_total_price}. We will process it shortly."
#     send_sms(user.profile.phone, message_for_customer)
#     print(send_sms)


#     admin_users = User.objects.filter(is_staff=True)  
#     message_for_admin = f"New order placed by {user.username}. Order total: ${final_total_price}."
#     print(message_for_admin)
    
 
#     for admin in admin_users:
#         send_sms(admin.profile.phone_number, message_for_admin)
    
   
#     Notification.objects.create(
#         user=user,
#         message=f"Your order has been placed. Total: ${final_total_price}.",
#         notification_type="order",
#         action_url="/order_details", 
#     )
    

#     for admin in admin_users:
#         Notification.objects.create(
#             user=None,  
#             message=f"New order placed by {user.username}. Total: ${final_total_price}.",
#             notification_type="admin",
#             action_url="/admin/orders",
#         )
#         print(f"Created Notification for Admin: {admin.username} - Order Total: ${final_total_price}")



def process_to_checkout(request):
    # Fetch all available products
    products = Product.objects.all()

    if request.method == 'POST':
        try:
            # Extract form data
            product_name = request.POST.get('product_name', '')
            name = request.POST.get('name', '')
            phone_number = request.POST.get('phone_number', '')
            email = request.POST.get('email', '')
            building = request.POST.get('building', '')
            locality = request.POST.get('locality', '')
            region = request.POST.get('region', '')
            city = request.POST.get('city', '')
            age = request.POST.get('age', '')
            total_price = request.POST.get('total_price', '0')  # Default to '0' if not provided

            # Validate and convert total_price
            try:
                total_price = float(total_price)  # Convert to a decimal number
            except ValueError:
                raise ValidationError("Total price must be a valid decimal number.")

            # Create a new order object
            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                product_name=product_name,
                name=name,
                phone_number=phone_number,
                email=email,
                building=building,
                locality=locality,
                region=region,
                city=city,
                age=age,
            )
            order.save()

            # Redirect to a success page or wherever necessary
            return redirect('customer:process_to_checkout')

        except ValidationError as e:
            # Handle validation errors and send error messages to the template
            context = {
                'products': products,
                'error_message': e.messages[0],  # Display the first validation error message
            }
            return render(request, 'customer/process_to_checkout.html', context)

    context = {
        'products': products,  # Pass products to the template
    }

    return render(request, 'customer/process_to_checkout.html', context)




def order(request):
    # Fetch all orders from the database
    orders = Order.objects.all()
    # Pass the orders in a dictionary as the context
    return render(request, 'customer/order.html', {'orders': orders})

def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'customer/order_confirmation.html', {'order': order})

PHONE_REGEX = r'^(?:\+88|88)?01[3-9]\d{8}$'
def sign_up(request):

    if request.method == 'POST':
    
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        location = request.POST.get('location')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        profile_image = request.FILES.get('profile_image')

 
        if not re.match(PHONE_REGEX, phone):
            messages.error(request, "Please enter a valid Bangladesh phone number.")
            return redirect('sign-up')

        if username and email and password:

            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} already exists')
                return redirect('sign-up')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, f'Email {email} already exists')
                return redirect('sign-up')
            
            user = User.objects.create_user(
                username=username,
                email=email, 
                password=password,
                first_name = first_name,
                last_name = last_name
            )
            if birth_date:
                try:
                    birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
                except ValueError:
                    messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
                    return redirect('sign-up')
                
            profile, created = Profile.objects.get_or_create(user=user)  

            profile.birth_date = birth_date
            profile.location = location
            profile.address = address
            profile.phone = phone
            profile.father_name = father_name
            profile.mother_name = mother_name
            profile.profile_image = profile_image
            profile.save()
            
            otp = str(random.randint(100000,999999))
            print(otp)

            user.profile.email_verification_code = otp
            user.profile.save()
            user.save()
            context = {
                'otp': otp,
                'username': username,
            }
            send_email('Your account has been created successfull', [email], 'customer/emails/email_activation.html', context, [])
            messages.success(request, 'Sign up successful. Please check your email for verification')
            return redirect('customer_home')

            # messages.success(request, "Your account has been created successfully.")
            # return redirect('management_home')  

        else:
            messages.error(request, "There was an error with your form submission.")
            return redirect('sign_up')

    return render(request, 'customer/user_management/sign_up.html')

def verify_email(request):
        

    if request.method == 'POST':
        otp = request.POST.get('otp')

        user_otp = Profile.objects.filter(email_verification_code=otp).first()

        if user_otp:
            user = User.objects.get(id=user_otp.user.id)

            if otp == user_otp.email_verification_code:
                auth_login(request, user)
                messages.success(request, "Login successful")
                return redirect('customer_home')
            else:
                messages.error(request, "Invalid OTP entered")
        else:
            messages.error(request, "Invalid OTP entered or user not found")


    return render(request, 'customer/user_management/verify_email.html')

def login(request):


    # if request.user.is_authenticated:
    #     return redirect('management_home')

    if request.method == 'POST':
   
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "Both fields are required.")
            return render(request, 'management/user_management/login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
                if user.is_superuser or user.is_staff:

                    # geneate random otp
                    if user :
                      
                        otp = random.randint(100000,999999)
                        print(otp)

                        user.profile.email_verification_code = otp
                        user.profile.save()
                        user.save()
                        context = {
                            'otp': otp,
                            'username':username
                        }
                        email = User.objects.get(username=username).email
                        send_email('Verify your account', [email], 'customer/emails/email_verification.html', context, [])
                        return redirect('verify_email')
        else:
                messages.error(request, 'Invalid username and password. ')  


    return render(request, 'customer/user_management/login.html')

def orders(request):
    all_orders = Order.objects.all()

    context = {
        'all_orders':all_orders
    }
    return render(request, 'customer/order_management/orders.html', context)

