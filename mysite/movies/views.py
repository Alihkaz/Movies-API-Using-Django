
#imports

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Moviedata

class MovieViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.all()
    serializer_class=MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.filter(type='action')
    serializer_class=MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.filter(type='comedy')
    serializer_class=MovieSerializer


class FantasiaViewSet(viewsets.ModelViewSet):
    queryset=Moviedata.objects.filter(type='fantasia')
    serializer_class=MovieSerializer    