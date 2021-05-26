from django.urls import path
from . import views

urlpatterns = [
    path('<int:category_id>',views.displaybyid,name='subcategory'),
    path('playlist', views.playlist, name='playlist'),
]