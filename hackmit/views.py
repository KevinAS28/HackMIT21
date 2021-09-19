from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.db import Error, IntegrityError
from django.db.transaction import atomic
from django.shortcuts import render, redirect

from hackmit.cockroach_views import *

from hackmit.ebook_tools import *
from text2emotion import get_emotion


def read_mode(request, book_id, page_num):
    chapters_paragraphs = epub2pea('ebooks/0.epub')
    pages = [page for chapter in chapters_paragraphs for page in chapter]
    texts = ' .\n '.join(pages[page_num])
    text_emotions_val = get_emotion(texts)
    # {'Angry': 0.0, 'Fear': 0.0, 'Happy': 0.8, 'Sad': 0.0, 'Surprise': 0.2}

    number_emotions = {
        0: 'Neutral | Focus',
        1: 'Happy',
        2: 'Angry',
        3: 'Surprise',
        4: 'Sad',
        5: 'Fear'
    }
    emotions_number = {val: key for key, val in number_emotions.items()}
    text_val_emotions = {val: key for key, val in text_emotions_val.items()}

    highest_emotion = text_val_emotions[sorted(text_val_emotions)]
    

    
        

    return render(request, 'read_mode.html', {'text': texts})
