from rest_framework import serializers
from api import models


class ClientSerializer(serializers.ModelSerializer):

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
        )


class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

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