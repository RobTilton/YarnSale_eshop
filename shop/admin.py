from django.contrib import admin
from .models import UserProfile, Product, ProductAttribute, Cart, CartItem, Order, OrderItem, Payment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(ProductAttribute)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)