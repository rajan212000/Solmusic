from django.shortcuts import render
from .models import Song
from Subcategory.models import Subcategory

def song(request, subcategory_id):
    subcategory = Subcategory.objects.get(id=subcategory_id)
    songs = Song.objects.filter(subcategory=subcategory_id)
    content = {
        'songs': songs,
        'subcategory': subcategory
    }
    return render(request,"solmusic/artist.html", content)

def searchsong(request):
    title = request.GET['stext']
    songs = Song.objects.filter(title__icontains=title)
    content = {
        'songs':songs,
        'value':title,
        'notfound':'Record Not Found'
    }
    return render(request,'solmusic/searchsong.html',content)

def play(request, song_id):
    song = Song.objects.get(id=song_id)
    content = {
        'song':song
    }
    print(song)
    return render(request,'solmusic/playsong.html', content)