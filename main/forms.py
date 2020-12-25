from django import forms
from .models import Post


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content']

    def save(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.instance.author = self.request.user 
        return super().save(*args, **kwargs)    
