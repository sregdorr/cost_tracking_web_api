from rest_framework import serializers
from api import models


class ClientSerializer(serializers.ModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='project-detail'
    )

    class Meta:
        model = models.Client
        fields = (
            'id',
            'url',
            'client_name',
            'address',
            'phone',
            'email',
            'created_date',
            'projects',
        )


class ClientNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = (
            'id',
            'url',
            'client_name',
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = (
            'id',
            'url',
            'client',
            'project_name',
            'project_number',
            'start_date',
            'end_date',
            'created_date',
        )


class ProjectReadSerializer(ProjectSerializer):
    client = ClientNestedSerializer(read_only=True)
