# anime_data/forms.py
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['rank', 'thai_title', 'eng_title', 'seasons', 'platform']
        widgets = {
            'platform': forms.TextInput(attrs={'pattern': '[a-zA-Zก-๙\s]+'}),
        }