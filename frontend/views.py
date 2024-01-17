from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from shop.models import Product


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
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})