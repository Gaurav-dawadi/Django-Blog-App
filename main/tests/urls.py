from main.models import Post
from django.urls import reverse, resolve
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from main.views import PostDetailView, PostCreateView, HomeView, PostUpdateView


class TestUrls(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'john12345')

    def test_login(self):
        self.client.login(username='john', password='john12345')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_home_url(self):
        # url = reverse('blog:home')
        # self.assertEqual(resolve(url).func.view_class, HomeView)
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)

    def test_create_url(self):
        # url = reverse('blog:create')
        # self.assertEqual(resolve(url).func.view_class, PostCreateView)
        response = self.client.get(reverse('blog:create'))
        self.assertEqual(response.status_code, 200)    

    def test_detail_url(self):
        response = self.client.get(reverse('blog:detail', args=['some-slug']))
        self.assertEqual(response.status_code, 200)
        # url = reverse('blog:detail', args=['some-slug'])
        # self.assertEqual(resolve(url).func.view_class, PostDetailView)  

    def test_update_url(self):
        response = self.client.get(reverse('blog:detail', args=[1]))
        self.assertEqual(response.status_code, 200)
        # url = reverse('blog:update', args=[1])
        # self.assertEqual(resolve(url).func.view_class, PostUpdateView)      
    