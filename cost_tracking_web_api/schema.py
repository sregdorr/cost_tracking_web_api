from api import schema
import graphene


class Query(schema.Query):
    pass

schema = graphene.Schema(query=Query)
