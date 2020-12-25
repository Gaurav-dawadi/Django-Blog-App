from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

# Create your models here.

USER = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(USER, on_delete=models.CASCADE)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)    

