# anime_data/models.py
from django.db import models
from django.core.validators import MinValueValidator

class Movie(models.Model):
    rank = models.IntegerField(validators=[MinValueValidator(1)])
    thai_title = models.CharField(max_length=200)
    eng_title = models.CharField(max_length=200)
    seasons = models.IntegerField(validators=[MinValueValidator(1)])
    platform = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rank}. {self.thai_title} ({self.eng_title})"