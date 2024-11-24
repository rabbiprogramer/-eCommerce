from django import forms
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, ProductImage


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone', 'email', 'address', 'country', 'city', 'state', 'zip', 'blood_group', 'profile_image', 'language']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

    # If you need additional validation (e.g., phone number format), you can override the field's clean method
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        # You can add custom validation here if needed
        return phone


class CustomSuperuserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superuser = True
        user.is_staff = True
        if commit:
            user.save()
        return user


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category', 'brand', 'title', 'description', 'vendor', 'price', 'sale_price', 
            'regular_price', 'add_stock', 'restock_quantity', 'shipping_fee', 'global_delivery', 
            'selected_countries', 'tags', 'collections', 'images', 'attributes', 'shipping_method', 
            'is_fragile', 'is_biodegradable', 'is_frozen', 'max_temperature', 'expiry_date', 
            'product_id_type', 'product_id', 'sku', 'color', 'size'
        ]
        widgets = {
            'shipping_method': forms.RadioSelect(choices=[('seller', 'Fulfilled by Seller'), ('admin', 'Fulfilled by Admin')]),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'sale_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'regular_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'add_stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'restock_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'shipping_fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'collections': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'attributes': forms.TextInput(attrs={'class': 'form-control'}),
            'shipping_method': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'is_fragile': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_biodegradable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
            'expiry_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'product_id_type': forms.Select(attrs={'class': 'form-control'}),
            'product_id': forms.TextInput(attrs={'class': 'form-control'}),
        }


