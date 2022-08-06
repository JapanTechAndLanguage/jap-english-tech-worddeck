from django.db import models

# Create your models here.
class Term(models.Model):
    kanji = models.CharField(max_length=150)
    kana = models.CharField(max_length=150)
    roomaji = models.CharField(max_length=150)
    english_text = models.CharField(max_length=150)
    japanese_audio_path = models.FileField()
    english_audio_path = models.FileField()


