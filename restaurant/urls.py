from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
     path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
