from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    abstract = models.TextField()
    content = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey('BlogCategory', null=True, blank=True, on_delete=models.CASCADE) 

    mainImage = models.ImageField(upload_to='')
    subImage1 = models.ImageField(upload_to='', null=True, blank=True)
    subImage2 = models.ImageField(upload_to='', null=True, blank=True)
    subImage3 = models.ImageField(upload_to='', null=True, blank=True)
    subImage4 = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['-datePosted']

class BlogCategory(models.Model):
    category = models.CharField(max_length=300)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

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

@receiver(pre_delete, sender=BlogPost)
def del_BlogPost(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    if instance.mainImage:
        instance.mainImage.delete(True)
    else:
        pass

    if instance.subImage1:
        instance.subImage1.delete(True)
    else:
        pass

    if instance.subImage2:
        instance.subImage2.delete(True)
    else:
        pass

    if instance.subImage3:
        instance.subImage3.delete(True)
    else:
        pass

    if instance.subImage4:
        instance.subImage4.delete(True)
    else:
        pass