# Problem: Django - Static Files and Media
# Description: Manage static files and handle media in a Django project.
# Code (settings.py):

# import os

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Problem: Django - Authentication and User Accounts
# Description: Implement user authentication and manage user accounts in a Django project.
# Code (views.py):

# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.shortcuts import render

# @login_required
# def profile(request):
#     return render(request, 'profile.html', {'user': request.user})

# Problem: Django - REST Framework (APIs)
# Description: Create a simple API using Django REST Framework.
# Code (serializers.py):

# from rest_framework import serializers
# from .models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'name', 'age']

# Problem: Django - Testing and Deployment
# - Description: Write tests for a Django project and deploy it to a hosting platform.
# - Code (tests.py):
