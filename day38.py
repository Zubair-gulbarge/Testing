# Problem: Web Development with Django

# Description: Create a simple web application using the Django framework.
# Code:

# Install Django: pip install django
# Create a new Django project: django-admin startproject myproject
# Create a new Django app: python manage.py startapp myapp

# Inside views.py (myapp/views.py)
# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("Hello, Django!")

# # Inside urls.py (myapp/urls.py)
# from django.urls import path
# from .views import hello

# urlpatterns = [
#     path('hello/', hello, name='hello'),
# ]

# # Inside myproject/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('myapp/', include('myapp.urls')),
# ]
