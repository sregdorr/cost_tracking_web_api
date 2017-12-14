from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.schemas import get_schema_view
from api import models
from api import serializers

schema_view = get_schema_view(title='Pastebin API')


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all().order_by('-created_date')
    serializer_class = serializers.ClientSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all().order_by('-created_date')
    serializer_class = serializers.ProjectSerializer


