
from django.contrib import admin
from django.urls import path

from mapapp import views
from mapapp.views import CctvList, CctvDetailList

urlpatterns = [
    path('', views.index),
    path('cctv/', CctvList.as_view()),
    path('cctv/<int:pk>/', CctvDetailList.as_view())
]
