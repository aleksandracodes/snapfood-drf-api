# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Post(models.Model):
    """
    A class for the post model
    """
    category_choices = [
        ('Spanish', 'Spanish'),
        ('Polish', 'Polish'),
        ('Portuguese', 'Portuguese'),
        ('Greek', 'Greek'),
        ('Italian', 'Italian'),
        ('Turkish', 'Turkish'),
        ('French', 'French'),
        ('Moroccan', 'Moroccan'),
        ('British', 'British'),
        ('German', 'German'),
        ('Austrian', 'Austrian'),
        ('Lebanese', 'Lebanese'),
        ('Caribbean', 'Caribbean'),
        ('Indian', 'Indian'),
        ('Thai', 'Thai'),
        ('Japanese', 'Japanese'),
        ('Chinese', 'Chinese'),
        ('Mexican', 'Mexican'),
        ('American', 'American'),
        ('Other', 'Other')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=category_choices)
    image = models.ImageField(
        upload_to='images/',
        default='../default_post_umaui6',
        blank=True
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
