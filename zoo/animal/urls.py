# step 3 : make a urls.py file and templates folder

from django.urls import path
from animal import views

urlpatterns = [
    # Step 4 : make a simple page
    path('page_a/',views.page_a),
    path('page_b/',views.page_b),
    path('page_c/',views.page_c),
    
    # Step 8 : Install bootstrap and base template
    # Step 9 : Create data
    path('create/', views.create),
    
    # step 10 : List page
    path('s',views.index),
    
    # step 11 Edit data
    path('edit/<animal_id>',views.edit),
    
    # step 12 : Delete data
    path('delete/<animal_id>',views.delete),
]
