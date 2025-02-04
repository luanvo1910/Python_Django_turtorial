from django.db import models

LAYOUT_CHOICE = (
    ('list', 'List'),
    ('grid', 'Grid')
)

STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('published', 'Published')
)

class Category(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    is_homepage = models.BooleanField(default=False)
    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICE, default='list')
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='draft')
    ordering = models.IntegerField(default=0)