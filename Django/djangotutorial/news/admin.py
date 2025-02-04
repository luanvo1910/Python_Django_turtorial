from django.contrib import admin

from .models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_homepage', 'layout', 'ordering')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
