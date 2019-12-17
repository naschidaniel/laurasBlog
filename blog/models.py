from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey('BlogCategory', null=True, blank=True, on_delete=False)
    slug = models.SlugField()
    
    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-datePosted']

class BlogCategory(models.Model):
    category = models.CharField(max_length=300)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=True)

    class Meta:
        unique_together = ('slug', 'parent')    
        verbose_name_plural = "BlogCategory"     
        ordering = ['category', 'parent__category']

    def __str__(self):                           
        full_path = [self.category]
        k = self.parent
        while k is not None:
            full_path.append(k.category)
            k = k.parent
        return ' -> '.join(full_path[::-1])