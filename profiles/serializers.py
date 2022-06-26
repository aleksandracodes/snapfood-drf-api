# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Profile
from followers.models import Follower
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProfileSerializer(serializers.ModelSerializer):
    """
    A class for a ProfileSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_number = serializers.ReadOnlyField()
    followers_number = serializers.ReadOnlyField()
    following_number = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Check if the logged-in user is following any of the other profiles
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'created_on',
            'updated_on',
            'image',
            'is_owner',
            'following_id',
            'posts_number',
            'followers_number',
            'following_number',
        ]
