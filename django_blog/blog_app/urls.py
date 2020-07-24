from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="blog-home"),
    path("post/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    path("post/create/", views.PostCreate.as_view(), name="create-post"),
    path("post/<int:pk>/update", views.PostUpdate.as_view(), name="update-post"),
    path("post/<int:pk>/delete", views.PostDelete.as_view(), name="delete-post"),
    path("user/<str:username>/", views.AllPostOfUser.as_view(),
         name="all-post-of-user")
]