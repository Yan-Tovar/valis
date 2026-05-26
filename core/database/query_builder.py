from sqlalchemy import or_


class QueryBuilder:


    @staticmethod
    def apply_filters(query, model, filters):

        if not filters:
            return query

        for field, value in filters.items():

            if hasattr(model, field):

                query = query.filter(
                    getattr(model, field) == value
                )

        return query


    @staticmethod
    def apply_search(
        query,
        model,
        search
    ):

        if not search:
            return query

        conditions = []

        for column in model.__table__.columns:

            if str(column.type).startswith("VARCHAR"):

                conditions.append(
                    getattr(model, column.name).ilike(
                        f"%{search}%"
                    )
                )

        if conditions:

            query = query.filter(
                or_(*conditions)
            )

        return query