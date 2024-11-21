from .models import *
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255, blank=True, null=True)
    fathers_name = models.CharField(max_length=255, blank=True, null=True)
    mothers_name = models.CharField(max_length=255, blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    profile_image = models.FileField(upload_to='profile_images/', blank=True, null=True)
    address = models.TextField(max_length=633, blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    blood_group = models.CharField(max_length=10, null=True, blank=True)
    role = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=10, null=True, blank=True)
    last_seen = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    Language = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.fathers_name or self.user.username} | Team {self.team_id or 'N/A'}"
class Category(models.Model):
    name = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

class Brand(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='brands')
    name = models.CharField(max_length=255)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name