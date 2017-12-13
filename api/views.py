from django.shortcuts import render
from rest_framework import viewsets
from api import models
from api import serializers


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all().order_by('-created_date')
    serializer_class = serializers.ClientSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all().order_by('-created_date')
    serializer_class = serializers.ProjectSerializer


