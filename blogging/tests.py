#Tests for the blogging app.

from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class PostTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        Post.objects.create(title="Sample Post", author=user)

    def test_post_creation(self):
        post = Post.objects.get(title="Sample Post")
        self.assertIsNotNone(post)
