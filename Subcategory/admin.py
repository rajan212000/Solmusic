from django.contrib import admin
from .models import Subcategory

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'description')
    list_display_links = ('id', 'name')
    list_filter = ('category',)

admin.site.register(Subcategory, SubcategoryAdmin)