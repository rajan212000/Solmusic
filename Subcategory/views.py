from django.shortcuts import render
from .models import Subcategory
from Category.models import Category

def displaybyid(request, category_id):
    subcategories = Subcategory.objects.filter(category=category_id)
    content = {
        'subcategories': subcategories
    }
    return render(request,'solmusic/subcategory.html', content)

def playlist(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    content = {
        'categories': categories,
        'subcategories': subcategories
    }
    return render(request,"solmusic/playlist.html", content)