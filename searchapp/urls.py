
from django.contrib import admin
from django.urls import path

from searchapp import views

urlpatterns = [
    path('', views.index),
]
