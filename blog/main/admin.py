from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'date_created', 'date_updated')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)