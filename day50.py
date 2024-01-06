# Problem: Django - Models and Database
# Description: Define models and perform database migrations in a Django project.
# Code (models.py):

# from django.db import models

# class User(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

# Problem: Django - Views and Templates
# Description: Create views and templates for a Django web application.
# Code (views.py):

# from django.shortcuts import render
# from .models import User

# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'user_list.html', {'users': users})

# Problem: Django - Forms and User Input
# Description: Implement forms and handle user input in a Django web application.
# Code (forms.py):

# from django import forms
# from .models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name', 'age']

# Problem: Django - URL Patterns and Navigation
# Description: Set up URL patterns and navigation in a Django project.
# Code (urls.py):
from django.urls import path
from .views import user_list

urlpatterns = [
    path('users/', user_list, name='user_list'),
]
