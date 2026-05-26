from database.connection import SessionLocal

from core.relationships.relationship_registry import (
    RelationshipRegistry
)


class RelationLoader:

    # ---------------------------------------------------------
    # GET NESTED ATTR
    # ---------------------------------------------------------

    @staticmethod
    def get_nested_attr(
        obj,
        path
    ):

        current = obj

        for part in path.split("."):

            if current is None:

                return ""

            current = getattr(
                current,
                part,
                None
            )

        return current

    # ---------------------------------------------------------
    # LOAD
    # ---------------------------------------------------------

    @staticmethod
    def load(page):

        session = SessionLocal()

        try:

            page.relation_data = {}

            for field_name, config in (
                RelationshipRegistry.RELATIONSHIPS.items()
            ):

                model = config["model"]

                label_field = config["label_field"]

                records = session.query(
                    model
                ).all()

                page.relation_data[field_name] = [

                    {
                        "id": item.id,

                        "label": str(

                            RelationLoader.get_nested_attr(
                                item,
                                label_field
                            )
                        )
                    }

                    for item in records
                ]

        finally:

            session.close()