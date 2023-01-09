import logging
import math

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from mapapp.models import Cctv
from mapapp.serializers import CctvSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response


def index(request):

    return render(request, 'mapapp/index.html')


class CctvList(generics.ListCreateAPIView):
    queryset = Cctv.objects.all()
    serializer_class = CctvSerializer

class CctvDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cctv.objects.all()
    serializer_class = CctvSerializer