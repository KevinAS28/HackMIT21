import os

from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static



from .views import *



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


    path('greetings/', lambda r: render(r, 'greetings.html'), name=f'greetings'),
    path('dashboard/', lambda r: render(r, 'dashboard.html'), name=f'dashboard'),

    path('read/<int:book_id>/<int:page_num>', read_mode, name='read_mode'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

print(os.getcwd())
for fname in os.listdir('hackmit/templates/unimplemented'):
    fname_wo_ext = fname.split(".")[-2]
    the_url = f'unimplemented/{fname_wo_ext}/'
    urlpatterns.append(path(the_url, lambda r: render(r, fname), name=f'unimplemented_{fname_wo_ext}'))
    print('Added ', fname, the_url)