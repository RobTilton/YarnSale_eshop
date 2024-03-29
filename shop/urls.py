from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserProfileViewSet, ProductViewSet, ProductAttributeViewSet, CartViewSet, CartItemViewSet, OrderViewSet, OrderItemViewSet, PaymentViewSet
 
router = DefaultRouter()
router.register(r'profile', UserProfileViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_attributes', ProductAttributeViewSet)
router.register(r'cart', CartViewSet)
router.register(r'cart_items', CartItemViewSet)
router.register(r'order', OrderViewSet)
router.register(r'ordered_items', OrderItemViewSet)
router.register(r'payment', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]