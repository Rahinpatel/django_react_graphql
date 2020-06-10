import graphene
import app.schema
import users.schema

class Query(users.schema.Alluser,
            users.schema.Query,
            
            app.schema.Query,
            
            graphene.ObjectType):
            pass

class Mutations(app.schema.Mutation,
            users.schema.Mutation,
            graphene.ObjectType):
            pass

schema = graphene.Schema(query=Query,mutation=Mutations)