from django.db import models
from tinymce.models import HTMLField
from .helpers import *
from .custom_field import *
from .define import *

class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    is_homepage = CustomBooleanField()
    layout = models.CharField(max_length=10, choices=APP_VALUE_LAYOUT_CHOICE, default=APP_VALUE_LAYOUT_DEFAULT)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'Categories'

class Article(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFAULT)
    special = CustomBooleanField()
    public_date = models.DateTimeField()
    content = HTMLField()
    image = models.ImageField(upload_to=get_file_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
class Feed(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICE, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    link = models.CharField(max_length=250)
