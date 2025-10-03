from django.shortcuts import render
from .models import MenuItem

def menu(request):
    items = MenuItem.objects.filter(available=True)
    return render(request, 'restaurant/menu.html', {'items': items})

def admin_dashboard(request):
    return render(request, 'restaurant/admin_dashboard.html')

