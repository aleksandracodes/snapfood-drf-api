# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from .models import Post
from .serializers import PostSerializer
from snapfood_drf_api.permissions import IsOwnerOrReadOnly
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PostList(generics.ListCreateAPIView):
    """
    A class view for the PostList
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        comments_number=Count(
            'comment',
            distinct=True
        ),
        likes_number=Count(
            'likes',
            distinct=True
        )
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'comments_number',
        'likes_number',
        'likes__created_on',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    filterset_fields = [
        'owner__followed__owner__profile',  # return specific user post feed
        'likes__owner__profile',  # return posts a specific user liked
        'owner__profile',  # return posts owned by a specific user
    ]

    def perform_create(self, serializer):
        """
        Method associates the post with the logged in user
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class view for post details
    to enable users to retrieve, update and delete the post
    """
    serializer_class = PostSerializer
    permission_classes = [
        IsOwnerOrReadOnly
        ]
    queryset = Post.objects.annotate(
        comments_number=Count(
            'comment',
            distinct=True
        ),
        likes_number=Count(
            'likes',
            distinct=True
        )
    ).order_by('-created_on')
