from django.contrib import admin
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'subcategory', 'title', 'status', 'format', 'singers', 'musiccompany')
    list_display_links = ('id', 'title')
    list_filter = ('subcategory',)

admin.site.register(Song, SongAdmin)