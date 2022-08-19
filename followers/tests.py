# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Follower
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class FollowerListViewTests(APITestCase):
    def setUp(self):
        """
        Automatically runs before every test method
        """
        User.objects.create_user(username='aleks', password='password')

    def test_not_logged_in_user_cannot_follow(self):
        """
        Test to ensure not logged-in user cannot follow others
        """
        response = self.client.post('/followers/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class FollowerDetailViewTests(APITestCase):
    def setUp(self):
        """
        Contains 3 users and 2 follows of 1st and 2nd user
        """
        aleks = User.objects.create_user(username='aleks', password='password')
        dave = User.objects.create_user(username='dave', password='password')
        mike = User.objects.create_user(username='mike', password='password')

        Follower.objects.create(owner=aleks, followed_id=2)  # 'id':1
        Follower.objects.create(owner=dave, followed_id=3)  # 'id':2

    def test_logged_in_user_can_follow_others(self):
        """
        Test to ensure logged-in user can follow others
        """
        self.client.login(username='aleks', password='password')
        response = self.client.post('/followers/', {'followed': 3})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_retrieve_existing_following(self):
        """
        Test if possible to retrieve a following by its valid ID
        """
        self.client.login(username='aleks', password='password')
        response = self.client.get('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_retrieve_non_existing_following(self):
        """
        Test if possible to retrieve a following with no valid ID
        """
        self.client.login(username='aleks', password='password')
        response = self.client.get('/followers/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_unfollow(self):
        """
        Test if user can unfollow user
        """
        self.client.login(username='aleks', password='password')
        response = self.client.delete('/followers/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_can_unfollow_other_user_follow(self):
        """
        Test if user can remove other user's following
        (unfollow a profile on someone else's behalf)
        """
        self.client.login(username='aleks', password='password')
        response = self.client.delete('/followers/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
