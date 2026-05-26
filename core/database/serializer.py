from sqlalchemy.inspection import inspect

from core.database.relationship_engine import (
    RelationshipEngine
)


class Serializer:

    # ---------------------------------------------------------
    # TO DICT
    # ---------------------------------------------------------

    @classmethod
    def to_dict(

        cls,

        instance,

        relationships=False,

        depth=1
    ):

        if instance is None:
            return None

        mapper = inspect(instance.__class__)

        data = {}

        # -----------------------------------------------------
        # COLUMNS
        # -----------------------------------------------------

        for column in mapper.columns:

            value = getattr(
                instance,
                column.key
            )

            data[column.key] = value

        # -----------------------------------------------------
        # RELATIONSHIPS
        # -----------------------------------------------------

        if relationships and depth > 0:

            relations = (
                RelationshipEngine
                .get_relationships(
                    instance.__class__
                )
            )

            for relation in relations:

                relation_name = (
                    relation["name"]
                )

                relation_value = getattr(
                    instance,
                    relation_name
                )

                # -------------------------------------------------
                # MANY
                # -------------------------------------------------

                if relation["uselist"]:

                    data[relation_name] = [

                        cls.to_dict(

                            item,

                            relationships=True,

                            depth=depth - 1
                        )

                        for item in relation_value
                    ]

                # -------------------------------------------------
                # ONE
                # -------------------------------------------------

                else:

                    data[relation_name] = (
                        cls.to_dict(

                            relation_value,

                            relationships=True,

                            depth=depth - 1
                        )
                    )

        return data

    # ---------------------------------------------------------
    # TO DICT LIST
    # ---------------------------------------------------------

    @classmethod
    def to_dict_list(

        cls,

        instances,

        relationships=False,

        depth=1
    ):

        return [

            cls.to_dict(

                instance,

                relationships=relationships,

                depth=depth
            )

            for instance in instances
        ]