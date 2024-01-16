from django.shortcuts import render
from shop.models import Product
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})