from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title_th', 'title_en', 'isbn', 'published_date', 'synopsis', 'store', 'price']

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if len(isbn) != 13:
            raise forms.ValidationError('ISBN must be 13 characters long.')
        return isbn
