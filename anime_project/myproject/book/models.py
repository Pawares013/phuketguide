from django.db import models

# Create your models here.
# models.py
# models.py
from django.db import models

class Book(models.Model):
    THAI_BOOKSTORES = [
        ('B2S', 'B2S'),
        ('NAIIN', 'นายอินทร์'),
        ('SEED', 'Se-ed'),
        ('MEB', 'Meb'),
    ]

    title_th = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateTimeField()
    synopsis = models.TextField()
    store = models.CharField(max_length=10, choices=THAI_BOOKSTORES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title_th
