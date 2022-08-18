# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Internal
from .models import Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        """
        Creates two users instances
        An associated profile instance is automatically created using a signal
        """
        User.objects.create_user(username='aleks', password='password')
        User.objects.create_user(username='dave', password='password')

    def test_user_can_view_existing_profile(self):
        """
        Test if possible to view existing profile (which has a valid ID)
        """
        self.client.login(username='aleks', password='password')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_view_non_existing_profile(self):
        """
        Test if possible to view a profile which doesn't exist
        (no valid ID)
        """
        self.client.login(username='aleks', password='password')
        response = self.client.get('/profiles/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_their_own_profile(self):
        """
        Test if user can update a profile they own
        """
        self.client.login(username='aleks', password='password')
        response = self.client.put('/profiles/1/',
                                   {'description': 'hello world'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.description, 'hello world')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_other_profiles(self):
        """
        Test if user cannot update other users' profiles
        """
        self.client.login(username='aleks', password='password')
        response = self.client.put('/profiles/2/', {'description': 'hi there'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_not_logged_in_user_can_update_their_own_profile(self):
        """
        Test if user can update their profile when not logged in
        """
        response = self.client.put('/profiles/1/',
                                   {'description': 'hello world'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_their_profile(self):
        """
        Test if user can delete their profile
        """
        self.client.login(username='aleks', password='password')
        response = self.client.delete('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
