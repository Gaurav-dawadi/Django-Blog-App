from django.urls import path
from .views import HomeView, PostDetailView, PostCreateView, PostUpdateView

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create', PostCreateView.as_view(), name='create'),
    path('<slug:slug>', PostDetailView.as_view(), name='detail'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='update')
]