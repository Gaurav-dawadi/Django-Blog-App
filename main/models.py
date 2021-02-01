from django.db import models
from datetime import date
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

GENDER_CHOICES = (
    ('select gender', 'Select Gender'),
    ('male', 'Male'),
    ('female', 'Female'),
    ('none', 'None')
)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default='select gender')
    about_me = models.TextField()

    def __str__(self):
        return self.full_name

    def calculate_age(self):
        age = date.today().year - self.dob.year
        return age   


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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

