# forms.py
from django import forms
from .models import Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title_thai', 'title_english', 'isbn', 'published_datetime', 'summary', 'store', 'price']
        widgets = {
            'published_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title_thai', css_class='form-group col-md-6 mb-0'),
                Column('title_english', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('isbn', css_class='form-group col-md-6 mb-0'),
                Column('published_datetime', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'summary',
            Row(
                Column('store', css_class='form-group col-md-6 mb-0'),
                Column('price', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'บันทึก', css_class='btn-primary')
        )