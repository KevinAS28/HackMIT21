# Generated by Django 3.2.7 on 2021-09-19 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackmit', '0002_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='converted_to_text',
        ),
        migrations.RemoveField(
            model_name='book',
            name='text_path',
        ),
    ]
