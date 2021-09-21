from .serializer import CompanySerializer
from companies.models import Company
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets

# Create your views here.
class ComanyModelViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer