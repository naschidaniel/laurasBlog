from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-datePosted']

class BlogMaincategorie(models.Model):
    maincategorie = models.CharField(max_length=300, unique=True, primary_key=True)
    allowSubcategorie = models.BooleanField(default=False)
    def __str__(self):
        return self.maincategorie

    class Meta:
        ordering = ['maincategorie']
    
class BlogSubcategorie(models.Model):
    maincategorie = models.ForeignKey(BlogMaincategorie, related_name="main", on_delete=models.CASCADE)
    subcategorie = models.CharField(max_length=300, default='---')
    def __str__(self):
        return "{} | {}".format(self.maincategorie, self.subcategorie)

    class Meta:
        ordering = ['maincategorie', 'subcategorie']