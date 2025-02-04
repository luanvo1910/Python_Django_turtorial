from django.contrib import admin

from .models import Category, Article

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_homepage', 'layout', 'ordering')
    list_filter = ['is_homepage', 'status', 'layout']
    search_fields = ['name']
admin.site.register(Category, CategoryAdmin)

class CategoryArtical(admin.ModelAdmin):
    list_display = ('name', 'status', 'special', 'public_date', 'category')
    list_filter = ['category', 'status', 'special']
    search_fields = ['name']
admin.site.register(Article, CategoryArtical)
