from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework import views, viewsets, status, generics, mixins
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from api.models import Client, Project
from api import serializers

schema_view = get_schema_view(title='Pastebin API')


class ClientViewSet(viewsets.ModelViewSet):
    """
    Viewset for listing or retrieving clients
    """
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = Client.objects.filter(id__lt=3)
    #     serializer = serializers.ClientSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    List all projects or create a new project
    """
    queryset = Project.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ('GET',):
            return serializers.ProjectReadSerializer
        return serializers.ProjectSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     data = serializer.data
    #     client = get_object_or_404(Client, id=serializer.data.get('client'))
    #     data.client = client
    #     return_serializer = serializers.ProjectReadSerializer(data=data, context={'request': request})
    #     return_serializer.is_valid(raise_exception=True)
    #
    #     headers = self.get_success_headers(return_serializer.data)
    #     return Response(return_serializer.data, status=status.HTTP_201_CREATED, headers=headers)





# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = models.Project.objects.all().order_by('-created_date')
#     serializer_class = serializers.ProjectSerializer


