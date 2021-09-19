import os
import copy

from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static as static_url



from .views import *

app_name = 'hackmit'

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
    path('home/', home, name=f'home'),

    path('read', read_mode, name='read'),

    path('read/<int:book_id>/<int:page_num>', read_mode, name='read_mode'),

    path('get_music/<int:emotions_number>/<int:previous_number>/', get_music, name='get_music_prev'),
    path('get_music/<int:emotions_number>/', get_music, name='get_music'),
    path('unimplemented/<str:fname>/', unimplemented, name='unimplemented'),
    path('prev_page/', prev_page, name='prev'),
    path('next_page/', next_page, name='next'),
    path('library/', lambda r:  render(r, 'library.html'), name='library'),

    path('', lambda r: render(r, 'login.html'), name='login'),
    

] + static_url(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 

# print(os.getcwd())
# for fname in os.listdir('hackmit/templates/unimplemented'):
#     fname_wo_ext = fname.replace('.', '_')
#     the_url = f'unimplemented/{fname_wo_ext}/'
#     urlpatterns.append(path(the_url, lambda r: render(r, copy.deepcopy(fname)), name=f'unimplemented_{fname_wo_ext}'))
#     print('Added ', fname, the_url)