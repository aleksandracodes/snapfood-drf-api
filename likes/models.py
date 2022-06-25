# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Internal:
from posts.models import Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Like(models.Model):
    """
    A class for the like model
    Related to 'owner' and 'posts'
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
        )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 'unique_together' prevents user from liking the same post twice
        unique_together = ['owner', 'post']
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.owner} {self.post}'
