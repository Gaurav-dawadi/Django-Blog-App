from django.urls import path
from .views import (UserRegistrationView, HomeView, PostDetailView, PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView)

app_name = 'blog'

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
    path('create', PostCreateView.as_view(), name='create'),
    path('users-blog', UserPostListView.as_view(), name='users_blog'),
    path('<slug:slug>', PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),
]