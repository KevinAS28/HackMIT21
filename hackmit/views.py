from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.db import Error, IntegrityError
from django.db.transaction import atomic
from django.shortcuts import render, redirect

from hackmit.cockroach_views import *

def read_mode(request, book_id):
    return render(request, 'read_mode.html', {'text': 'Hello world'})
