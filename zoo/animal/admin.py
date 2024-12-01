from django.contrib import admin

# Register your models here.


# Step 7 : make a admin panel
# python manage.py createsuperuser
from animal.models import Animal
admin.site.register(Animal)