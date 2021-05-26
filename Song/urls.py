from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('<int:subcategory_id>',views.song,name='song'),
    path('searchsong/', views.searchsong, name='searchsong'),
    path('play/<int:song_id>', views.play, name='play'),
]