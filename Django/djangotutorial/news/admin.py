from django.contrib import admin

from .models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_homepage', 'layout', 'ordering')
    list_filter = ['is_homepage', 'status', 'layout']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
