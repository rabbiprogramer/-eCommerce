from django.contrib import admin

# Register your models here.


from . models import *


admin .site.register(Profile)
admin .site.register(Product)
admin .site.register(Brand)
admin .site.register(SubCategory)
admin .site.register(Category)
admin .site.register(ProductImage)
admin .site.register(Collection)
admin .site.register(Vendor)
admin .site.register(Country)
admin .site.register(CartItem)