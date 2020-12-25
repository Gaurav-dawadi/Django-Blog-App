from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from main.views import user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='blog')),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
