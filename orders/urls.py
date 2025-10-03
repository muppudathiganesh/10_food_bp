from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]
