# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import generics, status, filters
from rest_framework.response import Response
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Profile
from .serializers import ProfileSerializer
from snapfood_drf_api.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ProfileList(generics.ListCreateAPIView):
    """
    A class view for the ProfileList
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_number=Count(
            'owner__post',
            distinct=True
        ),
        followers_number=Count(
            'owner__followed',
            distinct=True
            ),
        following_number=Count(
            'owner__following',
            distinct=True
        )
    ).order_by('-created_on')

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class for the Profile Detail
    """
    serializer_class = ProfileSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Profile.objects.all()

    def delete(self, request, pk):
        """
        Delete a profile by id
        """
        user = self.request.user
        user.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
