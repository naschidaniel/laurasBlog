from django.db import models

class SocialMediaLink(models.Model):
    socialMediaPlatform = models.CharField(max_length=250)
    url = models.URLField()

    class Meta:
        unique_together = ('socialMediaPlatform', 'url')    
        verbose_name_plural = "SocialMediaLink"     
        ordering = ['socialMediaPlatform', 'url']

    def __str__(self):
        return '{}'.format(self.socialMediaPlatform)
