import os
import re
import random

from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.db import Error, IntegrityError
from django.db.transaction import atomic
from django.shortcuts import render, redirect
from django.urls import reverse
from django.templatetags.static import static
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlencode


from hackmit.cockroach_views import *
from hackmit.models import *

from hackmit.ebook_tools import *
from text2emotion import get_emotion

global page_number, end_page
page_number = 0
end_page = 10

def read_mode(request, book_id=0, page_num=0):
    global page_number
    page_number = page_num

    book = list(Book.objects.filter(id=book_id))[0]

    chapters_paragraphs = epub2pea(book.file_path)
    pages = [page for chapter in chapters_paragraphs for page in chapter]
    texts = '. '.join(pages[page_num])
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
    highest_emotion = text_val_emotions[sorted(text_val_emotions)[-1]]
    print(emotions_number[highest_emotion])
    audio_url = get_music(request, emotions_number[highest_emotion], http_response=False, full_url=False)
    print(audio_url)
    return render(request, 'read_mode.html', {'text': texts, 'audio_url': '../..'+audio_url, 'mood_number': int(emotions_number[highest_emotion])})

def prev_page(request, book_id=0):
    global page_number
    if page_number > 0:
        page_number -= 1
    # return redirect('hackmit.views.prev_page', book_id=book_id, page_num=page_number)
    return redirect(f'../read/{book_id}/{page_number}')

def next_page(request, book_id=0):
    global page_number
    if page_number < end_page:
        page_number += 1
    # return redirect('hackmit.views.next_page', book_id=book_id, page_num=page_number)

    return redirect(f'../read/{book_id}/{page_number}')


def get_music(request, emotions_number, previous_number=None, http_response=True, full_url=True):
    music_files = os.listdir(f"{settings.BASE_DIR}/hackmit/static/musics")
    music_emotions = []
    for fname in music_files:
        re_result = re.search(r'(\d+)_(\d+)_', fname)
        if not re_result:
            continue
        emotions, music_index = re_result.groups()
        if int(emotions_number)==int(emotions):
            music_emotions.append([fname, re_result])
    music_emotions = random.sample(music_emotions, len(music_emotions))
    for fname, re_result in music_emotions:
        if not (previous_number is None):
            emotions, music_index = re_result.groups()
            if previous_number==music_index:
                continue
        if full_url:
            music_url = get_current_site(request).domain+static(f'musics/{fname}')
        else:
            music_url = static(f'musics/{fname}')
        
        if http_response:
            # return HttpResponse(music_url)        
            return JsonResponse({'music_url': music_url})
        else:
            return str(music_url)

def unimplemented(request, fname):
    fname = fname.replace('_', '.')
    return render(request, fname)


def home(request):
    books = list(Book.objects.all())
    book_urls = [
        'https://www.duniadosen.com/wp-content/uploads/2020/11/stack-various-books-table-scaled-e1617270355396.jpg',
        'https://www.duniadosen.com/wp-content/uploads/2021/01/shutterstock_112295444.jpg',
        'https://iapi.or.id//uploads/article/100-book.png',
        
    ]*4
    return render(request, 'home.html', {'book_titles_ids': [(i, book.nick_name, book_urls[i]) for i, book in enumerate(books[:1])], 'book_titles': [i.nick_name for i in books[:4]], 'book_ids': [i.id for i in books[:4]]})
