from django.shortcuts import render
from .models import Category
from Song.models import Song

def index(request):
    categories = Category.objects.all()
    content = {
        'categories': categories
    }
    return render(request,'solmusic/index.html', content)

def categorypage(request):
    categories = Category.objects.all()
    songs = Song.objects.all()
    content = {
        'categories': categories,
        'songs': songs
    }
    return render(request,'solmusic/category.html', content)

def searchpage(request):
    return render(request,'solmusic/searchsong.html')

def blogpage(request):
    return render(request,'solmusic/blog.html')

def contactpage(request):
    return render(request,'solmusic/contact.html')
