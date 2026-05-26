from sqlalchemy.inspection import inspect


class RelationshipEngine:


    # ---------------------------------------------------------
    # GET RELATIONSHIPS
    # ---------------------------------------------------------

    @staticmethod
    def get_relationships(model):

        mapper = inspect(model)

        relationships = []

        for relation in mapper.relationships:

            local_column = None

            for column in relation.local_columns:

                local_column = column.name
                break

            relationships.append({

                "name": relation.key,

                "field": local_column,

                "target_model": relation.mapper.class_,

                "target_table": (
                    relation.mapper.class_.__tablename__
                ),

                "uselist": relation.uselist
            })

        return relationships


    # ---------------------------------------------------------
    # GET RELATIONSHIP MAP
    # ---------------------------------------------------------

    @classmethod
    def get_relationship_map(
        cls,
        model
    ):

        relationships = cls.get_relationships(
            model
        )

        mapping = {}

        for relation in relationships:

            mapping[
                relation["field"]
            ] = relation

        return mapping


    # ---------------------------------------------------------
    # IS FOREIGN KEY
    # ---------------------------------------------------------

    @classmethod
    def is_foreign_key(
        cls,
        model,
        field_name
    ):

        relationships = cls.get_relationship_map(
            model
        )

        return field_name in relationships


    # ---------------------------------------------------------
    # GET RELATED MODEL
    # ---------------------------------------------------------

    @classmethod
    def get_related_model(
        cls,
        model,
        field_name
    ):

        relationships = cls.get_relationship_map(
            model
        )

        relation = relationships.get(
            field_name
        )

        if not relation:
            return None

        return relation["target_model"]


    # ---------------------------------------------------------
    # GET DISPLAY FIELD
    # ---------------------------------------------------------

    @staticmethod
    def get_display_field(model):

        priority_fields = [

            "nombre",

            "nombre_completo",

            "descripcion",

            "titulo",

            "codigo",

            "codigo_cups"
        ]

        mapper = inspect(model)

        column_names = [

            column.name
            for column in mapper.columns
        ]

        for field in priority_fields:

            if field in column_names:

                return field

        return "id"