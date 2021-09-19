from django.db import models
import uuid

from hackmit.cockroach_model import *

class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    nick_name = models.CharField(max_length=50, blank=False)
    file_path = models.CharField(max_length=50, blank=False)
    converted_to_text = models.BooleanField(blank=False)
    text_path = models.CharField(max_length=50, blank=True)