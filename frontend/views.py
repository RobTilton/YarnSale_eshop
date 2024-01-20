from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from shop.models import Product, ProductAttribute, Cart, CartItem
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.utils import timezone

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

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

def view_cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
    except Cart.DoesNotExist:
        cart_items = []

    for item in cart_items:
        item.total_price = item.quantity * item.product.price

    total_cost = 0
    try:
        cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            item.total_price = item.quantity * item.product.price
            total_cost += item.total_price
    except Cart.DoesNotExist:
        cart_items = []

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_cost': total_cost})

@require_POST
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user, defaults={'created_date': timezone.now()})
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, defaults={'quantity': 1})
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({'status': 'success', 'cart_item_quantity': cart_item.quantity})

