from django.test import TestCase
from .forms import PostForm
from .models import Post

class PostFormTest(TestCase):
    def setUp(self):
        Post.objects.create(Title="lion")
        Post.objects.create(content="")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        title = Post.objects.get(title="lion")
        content = Post.objects.get(content="")
        self.assertEqual(title())
        self.assertEqual(content())
