from django.contrib import admin
from .models import BlogPost, BlogMaincategorie, BlogSubcategorie

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogMaincategorie)
admin.site.register(BlogSubcategorie)