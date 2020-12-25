from django.test import TestCase, Client
from django.urls import reverse, resolve
from main.views import PostDetailView

client = Client()

class TestUrls(TestCase):
    def test_home_url(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)

    def test_create_url(self):
        response = self.client.get(reverse('blog:create'))
        self.assertEqual(response.status_code, 200)    

    def test_detail_url(self):
        url = reverse('blog:detail', args=['some-slug'])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)   
    