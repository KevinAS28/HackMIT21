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
from django.templatetags.static import static
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


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
    highest_emotion = text_val_emotions[sorted(text_val_emotions)[-1]]
    print(emotions_number[highest_emotion])
    audio_url = get_music(request, emotions_number[highest_emotion], http_response=False)
    print(audio_url)
    return render(request, 'read_mode.html', {'text': texts, 'audio_url': audio_url})

def get_music(request, emotions_number, previous_number=None, http_response=True):
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
        music_url = get_current_site(request).domain+static(f'musics/{fname}')
        
        if http_response:
            return HttpResponse(music_url)        
        else:
            return str(music_url)
    