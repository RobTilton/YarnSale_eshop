from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from shop.models import Product, ProductAttribute


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send an email or save the data to your database
        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [settings.RECIPIENT_ADDRESS],
        #     fail_silently=False,
        # )

        
        messages.success(request, 'Your message has been sent!')
        return redirect('contact')

    return render(request, 'contact.html')

def shop(request):
    query = request.GET.get('q')
    if query:
        # Start with a distinct QuerySet of products
        products = Product.objects.distinct()
        # Filter products by name or their attributes
        products = products.filter(
            name__icontains=query
        ).distinct() | products.filter(
            attributes__name__icontains=query
        ).distinct() | products.filter(
            attributes__value__icontains=query
        ).distinct()
    else:
        products = Product.objects.all()

    return render(request, 'shop.html', {'products': products})