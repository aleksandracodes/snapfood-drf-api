# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Like
from posts.models import Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LikeListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='aleks', password='password')

    def test_not_logged_in_user_cannot_like_post(self):
        """
        Test to ensure not logged-in user cannot like post
        """
        response = self.client.post('/likes/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class LikeDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains two users, 3 posts and 2 like for 1st and 2nd post
        """
        aleks = User.objects.create_user(username='aleks', password='password')
        dave = User.objects.create_user(username='dave', password='password')
        Post.objects.create(
            owner=aleks, title='post title',
            description='test', category='Polish'
        )
        Post.objects.create(
            owner=dave, title='post title2',
            description='test2', category='Spanish'
        )
        Post.objects.create(
            owner=dave, title='post title3',
            description='test3', category='Greek'
        )
        Like.objects.create(owner=aleks, post_id=2)  # 'id':1
        Like.objects.create(owner=dave, post_id=1)  # 'id':2

    def test_logged_in_user_can_like_post(self):
        """
        Test to ensure logged-in user can create a comment
        """
        self.client.login(username='aleks', password='password')
        response = self.client.post('/likes/', {'post': 3})  # 'id':3
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_retrieve_existing_like(self):
        """
        Test if possible to retrieve a like by its valid ID
        """
        self.client.login(username='aleks', password='password')
        response = self.client.get('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_non_existing_like(self):
        """
        Test if possible to retrieve a like with no valid ID
        """
        self.client.login(username='aleks', password='password')
        response = self.client.get('/likes/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unlike_own_like(self):
        """
        Test if user can remove like (unlike a post)
        """
        self.client.login(username='aleks', password='password')
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_unlike_other_user_like(self):
        """
        Test if user can remove someone else's like
        (unlike a post for someone)
        """
        self.client.login(username='aleks', password='password')
        response = self.client.delete('/likes/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
