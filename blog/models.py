from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(default='', max_length=255)
    description = models.TextField(default='', blank=True)
    slug = models.SlugField(default='', blank=True, max_length=255)
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title

    # slug is a short label thet is used in URLs, it can only use letters, numbers,hyphens and underscores
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.slug)])
 
    
