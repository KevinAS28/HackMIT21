import os

from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect

from .views import CustomersView, OrdersView, PingView, ProductView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ping/', PingView.as_view()),

    # Endpoints for customers URL.
    path('customer/', CustomersView.as_view(), name='customers'),
    path('customer/<uuid:id>/', CustomersView.as_view(), name='customers'),

    # Endpoints for customers URL.
    path('product/', ProductView.as_view(), name='product'),
    path('product/<uuid:id>/', ProductView.as_view(), name='product'),

    path('order/', OrdersView.as_view(), name='order'),
]

print(os.getcwd())
for fname in os.listdir('hackmit/templates/unimplemented'):
    the_url = f'unimplemented/{fname.split(".")[-2]}/'
    urlpatterns.append(path(the_url, lambda r: render(r, fname)))
    print('Added ', the_url)