from sqlalchemy.inspection import inspect


class RelationshipInspector:


    @staticmethod
    def get_relationships(model):

        mapper = inspect(model)

        return mapper.relationships


    @staticmethod
    def has_related_records(instance):

        mapper = inspect(instance.__class__)

        for relation in mapper.relationships:

            related = getattr(instance, relation.key)

            if related:

                return True

        return False