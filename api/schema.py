import graphene
from graphene import Node
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from api import models


class EntityInterface(graphene.Interface):
    db_id = graphene.String()

    def resolve_db_id(self, info, **kwargs):
        return self.id


class ClientType(DjangoObjectType):
    class Meta:
        model = models.Client
        filter_fields = ( 'client_name',)
        interfaces = (EntityInterface, Node)


class ProjectType(DjangoObjectType):
    class Meta:
        model = models.Project
        filter_fields = ('project_name',)
        interfaces = (EntityInterface, Node)


class Query(graphene.ObjectType):
    class Meta:
        abstract = True

    client = Node.Field(ClientType)
    all_clients = DjangoFilterConnectionField(ClientType)

    project = Node.Field(ProjectType)
    all_projects = DjangoFilterConnectionField(ProjectType)