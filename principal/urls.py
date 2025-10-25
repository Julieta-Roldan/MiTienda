from django.urls import path
from . import views

app_name = 'principal'

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('category/', views.category, name='category'),
    path('contact/', views.contact, name='contact'),
    path('product/<slug:slug>/', views.single_product, name='single_product'),  # si usás slugs
    # Auth
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # Panel vendedor
    path('panel-vendedor/', views.panel_vendedor, name='panel_vendedor'),
]
