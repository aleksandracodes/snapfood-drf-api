# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@api_view()
def home(request):
    return Response({
        'status': 200,
        'message': "Hi there, welcome to SnapFood Django REST Framework API"
        })
