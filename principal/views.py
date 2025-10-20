from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def inicio(request):
    return render(request, 'principal/index.html')

def cart(request):
    return render(request, 'principal/cart.html')

def category(request):
    return render(request, 'principal/category.html')

def contact(request):
    return render(request, 'principal/contact.html')

def login_view(request):
    return render(request, 'principal/login.html')

def single_product(request):
    return render(request, 'principal/single-product.html')
