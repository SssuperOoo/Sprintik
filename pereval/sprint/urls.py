from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers




urlpatterns = [
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]