from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name= 'index'),
    path('upload/', views.upload, name= 'upload'),
 
]
