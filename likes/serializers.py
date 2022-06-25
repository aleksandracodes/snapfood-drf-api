# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import IntegrityError
from rest_framework import serializers

# Internal:
from .models import Like
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LikeSerializer(serializers.ModelSerializer):
    """
    A class for a LikeSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id',
            'owner',
            'created_on',
            'post',
        ]

    def create(self, validated_data):
        """
        Handle possible duplicates of likes by the same user
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplication'
            })
