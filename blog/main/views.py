from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm, LoginForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

def user_login(request):
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog:home')
        else:
            messages.error(request, 'Credentials doesnot match OR User doesnot exists')
            return redirect('login')  

    context = {'form': form}
    return render(request, 'login.html', context)          


class CheckRequestUser(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('login')  


class HomeView(CheckRequestUser, ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'


class PostCreateView(CheckRequestUser, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    success_url = reverse_lazy('blog:home')


class PostDetailView(CheckRequestUser, DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

    
