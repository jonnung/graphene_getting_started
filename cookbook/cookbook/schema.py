import graphene

from ingredients.schema import Query as IngredientsQuery


class Query(IngredientsQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)