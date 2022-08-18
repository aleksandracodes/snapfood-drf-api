# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PostListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='aleks', password='password')

    def test_not_logged_in_user_cannot_create_post(self):
        """
        Test to ensure not logged-in user cannot create a post
        """
        response = self.client.post('/posts/', {'category': 'Spanish'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_create_post(self):
        """
        Test to ensure logged-in user can create a post
        """
        self.client.login(username='aleks', password='password')
        response = self.client.post('/posts/', {'title': 'post title',
                                                'category': 'Spanish'})
        # print('response:', response.data)
        post_count = Post.objects.count()
        self.assertEqual(post_count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

