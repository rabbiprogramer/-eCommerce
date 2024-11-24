from .models import *
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from django.core.validators import RegexValidator  

class Profile(models.Model):
 
    bangladeshi_phone_validator = RegexValidator(
        regex=r'^(013|014|015|016|017|018|019)\d{8}$',
        message="Enter a valid Bangladeshi phone number (11 digits starting with 013-019)."
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    profile_image = models.FileField(upload_to='profile_images/', blank=True, null=True)
    address = models.TextField(max_length=633, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True, validators=[bangladeshi_phone_validator])
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.user.username

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Vendor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey('Product', related_name='product_images', on_delete=models.CASCADE)

    def __str__(self):
        return f"Image for {self.product.title}"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', default=1) 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    add_stock = models.PositiveIntegerField(default=0) 
    restock_quantity = models.PositiveIntegerField(default=0)
    shipping_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    global_delivery = models.BooleanField(default=False)
    selected_countries = models.ManyToManyField('Country', blank=True, related_name='products_in_country') 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tags = models.CharField(max_length=100, unique=True)
    collections = models.ManyToManyField(Collection, related_name='products', blank=True)  
    updated = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to='product_images/') 
    attributes = models.JSONField(null=True, blank=True, help_text="Product's extra attributes like size, color, etc.")
    shipping_method = models.CharField(max_length=50, choices=[('seller', 'Fulfilled by Seller'), ('admin', 'Fulfilled by Admin')], default='admin')
    is_fragile = models.BooleanField(default=False)
    is_biodegradable = models.BooleanField(default=False)
    is_frozen = models.CharField(max_length=255, null=True, blank=True)
    max_temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    expiry_date =  models.DateTimeField(null=True, blank=True)
    product_id_type = models.CharField(max_length=20, choices=[('ISBN', 'ISBN'), ('UPC', 'UPC'), ('EAN', 'EAN'), ('JAN', 'JAN')], default='ISBN')
    product_id = models.CharField(max_length=255, null=True, blank=True)

    sku = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=100, null=True, blank=True) 
    size = models.CharField(max_length=50, null=True, blank=True) 

    def __str__(self):
        return self.title or self.sku


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



