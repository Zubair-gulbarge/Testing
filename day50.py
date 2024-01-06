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
