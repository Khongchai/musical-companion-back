import graphene
from graphql_auth.schema import UserQuery

from ecommerce.graphene_queries.me_queries_extended import MeQueryExtended

from .graphene_mutations.cart_mutations import CartMutations
from .graphene_mutations.user_mutations import (AuthMutations,
                                                CustomAuthMutations)
from .graphene_queries.cart_queries import CartsQuery
from .graphene_queries.store_queries import (ComposersQuery, CompositionsQuery,
                                             DataAfterPurchaseQuery,
                                             ProductsQuery)


class Query(UserQuery, MeQueryExtended, ComposersQuery, ProductsQuery, 
            CompositionsQuery, DataAfterPurchaseQuery, 
            CartsQuery, graphene.ObjectType):
    pass
class Mutation(AuthMutations, CustomAuthMutations, CartMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)


