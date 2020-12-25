from .models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from .forms import PostForm, LoginForm, RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
# from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView,
                                    DeleteView)

# Create your views here.

class UserRegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


def user_login(request):
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
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
    ordering = '-id'


class PostCreateView(CheckRequestUser, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Blog was successfully created')
        return super().form_valid(form)


class PostDetailView(CheckRequestUser, DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class PostUpdateView(CheckRequestUser, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Blog sucessfully updated')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  

    def get_success_url(self, *args, **kwargs):
        post = self.get_object()
        return reverse('blog:detail', args=[post.slug])    


class PostDeleteView(CheckRequestUser, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

    def get_success_url(self):
        messages.success(self.request, 'Blog was sucessfully deleted')
        return reverse('blog:home')       


class UserPostListView(CheckRequestUser, ListView):
    model = Post
    template_name = 'users_blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user_obj = self.request.user
        posts = Post.objects.filter(author=user_obj).order_by('-id')
        return posts 