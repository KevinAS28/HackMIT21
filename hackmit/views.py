from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.db import Error, IntegrityError
from django.db.transaction import atomic
from django.shortcuts import render, redirect

from hackmit.cockroach_views import *

from hackmit.ebook_tools import *

def read_mode(request, book_id, page_num):
    open('ebooks/0.epub')
    chapters_paragraphs = epub2pea('ebooks/0.epub')
    pages = [page for chapter in chapters_paragraphs for page in chapter]
    texts = ' .\n '.join(pages[page_num])
    return render(request, 'read_mode.html', {'text': texts})
