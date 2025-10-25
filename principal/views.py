from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy

# Vista principal (index)
def index(request):
    return render(request, 'principal/index.html')

# si ya tenías estas vistas (cart, category, contact, single_product) mantenelas
# ejemplo:
def cart(request):
    return render(request, 'principal/cart.html')

def category(request):
    return render(request, 'principal/category.html')

def contact(request):
    return render(request, 'principal/contact.html')

def single_product(request, slug=None):
    return render(request, 'principal/single-product.html')

# Login / Logout (usando las clases de Django)
class LoginView(auth_views.LoginView):
    template_name = 'principal/login.html'

class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('principal:index')

# Panel vendedor: permite solo a usuarios en grupo "Vendedores"
def es_vendedor(user):
    return user.is_authenticated and user.groups.filter(name='Vendedores').exists()

@login_required
@user_passes_test(es_vendedor)
def panel_vendedor(request):
    return render(request, 'principal/panel_vendedor.html')


# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render

# def inicio(request):
#     return render(request, 'principal/index.html')

# def cart(request):
#     return render(request, 'principal/cart.html')

# def category(request):
#     return render(request, 'principal/category.html')

# def contact(request):
#     return render(request, 'principal/contact.html')

# def login_view(request):
#     return render(request, 'principal/login.html')

# def single_product(request):
#     return render(request, 'principal/single-product.html')
