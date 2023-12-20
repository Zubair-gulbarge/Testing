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

# Problem: Neural Network with TensorFlow

# Description: Implement a simple neural network using the TensorFlow library.
# Code:

# import tensorflow as tf
# from tensorflow.keras import layers, models

# # Sample data (replace with your dataset)
# (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# # Normalize pixel values to be between 0 and 1
# train_images, test_images = train_images / 255.0, test_images / 255.0

# # Build a simple neural network
# model = models.Sequential([
#     layers.Flatten(input_shape=(28, 28)),
#     layers.Dense(128, activation='relu'),
#     layers.Dropout(0.2),
#     layers.Dense(10)
# ])

# # Compile the model
# model.compile(optimizer='adam',
#               loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#               metrics=['accuracy'])

# # Train the model
# model.fit(train_images, train_labels, epochs=5)

# # Evaluate the model
# test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
# print(f'Test accuracy: {test_acc}')
