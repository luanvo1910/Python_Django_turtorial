from django.db import models
from tinymce.models import HTMLField
from .helpers import *

class Category(models.Model):
    LAYOUT_CHOICE = (
        ('list', 'List'),
        ('grid', 'Grid')
    )
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    is_homepage = models.BooleanField(default=False)
    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICE, default='list')
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Article(models.Model):
    STATUS_CHOICE = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    special = models.BooleanField(default=False)
    public_date = models.DateTimeField()
    content = HTMLField()
    image = models.ImageField(upload_to=get_file_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    