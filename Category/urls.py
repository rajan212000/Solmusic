from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('category/',views.categorypage,name='category'),
    path('search/',views.searchpage,name='search'),
    path('blog/',views.blogpage,name='blog'),
    path('contact/',views.contactpage,name='contact'),
]