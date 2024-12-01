# anime_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('anime_data.urls')),
]

# anime_data/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_anime/', views.add_anime, name='add_anime'),
    path('anime_list/', views.anime_list, name='anime_list'),
]