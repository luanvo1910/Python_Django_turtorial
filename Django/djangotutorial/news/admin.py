from django.contrib import admin
from .models import Category, Article, Feed
from .define import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_homepage', 'layout', 'ordering')
    list_filter = ['is_homepage', 'status', 'layout']
    search_fields = ['name']
    class Media: 
        css = {'all' : ('admin/css/custom.css',)}

class ArticalAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'special', 'public_date', 'category')
    list_filter = ['category', 'status', 'special']
    search_fields = ['name']   
    class Media: 
        css = ADMIN_SRC_CSS

class FeedAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_filter = ['status']
    search_fields = ['name', 'link']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticalAdmin)
admin.site.register(Feed, FeedAdmin)

admin.site.site_header = ADMIN_HEADER_NAME