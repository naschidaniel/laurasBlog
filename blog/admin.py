from django.contrib import admin
from .models import BlogPost, BlogCategory, BlogQuote

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogQuote)
admin.site.register(BlogCategory)
