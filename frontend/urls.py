from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]