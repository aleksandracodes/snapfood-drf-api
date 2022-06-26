# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from rest_framework import serializers

# Internal:
from .models import Post
from likes.models import Like
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PostSerializer(serializers.ModelSerializer):
    """
    A class for a PostSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        """
        Validation of the uploaded image size
        """
        # Image height limit of 4096 px
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Your image exceeds the height limit of 4096px.'
            )

        # Image width limit of 4096 px
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Your image exceeds the width limit of 4096px.'
            )

        # Image size limit of 2 megabytes
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Your image is too large. Max size is 2MB.'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_on',
            'updated_on',
            'title',
            'description',
            'category',
            'image',
            'like_id',
        ]
