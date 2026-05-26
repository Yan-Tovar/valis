from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy.inspection import inspect
from sqlalchemy.sql.sqltypes import Date, Integer, Float

from core.database.base_crud import (
    BaseCRUD
)


class BaseRepository:


    def __init__(
        self,
        model,
        session: Session
    ):

        self.model = model

        self.session = session

        self.crud = BaseCRUD(
            self.session
        )

    # ---------------------------------------------------------
    # PARSE DATES
    # ---------------------------------------------------------

    def _parse_dates(
        self,
        data
    ):

        mapper = inspect(
            self.model
        )

        for column in mapper.columns:

            if isinstance(
                column.type,
                Date
            ):

                value = data.get(
                    column.name
                )

                if (
                    value
                    and isinstance(
                        value,
                        str
                    )
                ):

                    try:

                        data[column.name] = (
                            datetime.strptime(
                                value,
                                "%Y-%m-%d"
                            ).date()
                        )

                    except Exception:

                        pass

        return data

    # ---------------------------------------------------------
    # PARSE INTEGERS
    # ---------------------------------------------------------

    def _parse_integers(
        self,
        data
    ):

        mapper = inspect(
            self.model
        )

        for column in mapper.columns:

            if isinstance(
                column.type,
                Integer
            ):

                value = data.get(
                    column.name
                )

                if (
                    value is not None
                    and value != ""
                    and isinstance(
                        value,
                        str
                    )
                ):

                    try:

                        data[column.name] = int(
                            value
                        )

                    except Exception:

                        pass

        return data

    # ---------------------------------------------------------
    # PARSE FLOATS
    # ---------------------------------------------------------

    def _parse_floats(
        self,
        data
    ):

        mapper = inspect(
            self.model
        )

        for column in mapper.columns:

            if isinstance(
                column.type,
                Float
            ):

                value = data.get(
                    column.name
                )

                if (
                    value is not None
                    and value != ""
                    and isinstance(
                        value,
                        str
                    )
                ):

                    try:

                        data[column.name] = float(
                            value
                        )

                    except Exception:

                        pass

        return data

    # ---------------------------------------------------------
    # CREATE
    # ---------------------------------------------------------

    def create(
        self,
        data
    ):

        data = self._parse_dates(
            data
        )
        data = self._parse_integers(
            data
        )
        data = self._parse_floats(
            data
        )

        return self.crud.create(
            self.model,
            data
        )

    # ---------------------------------------------------------
    # UPDATE
    # ---------------------------------------------------------

    def update(
        self,
        instance_id,
        data
    ):

        data = self._parse_dates(
            data
        )

        data = self._parse_integers(
            data
        )
        data = self._parse_floats(
            data
        )

        return self.crud.update(
            self.model,
            instance_id,
            data
        )

    # ---------------------------------------------------------
    # GET ALL
    # ---------------------------------------------------------

    def get_all(
        self,
        include_inactive=False,
        filters=None,
        search=None
    ):

        return self.crud.get_all(
            self.model,
            include_inactive,
            filters,
            search
        )

    # ---------------------------------------------------------
    # GET BY ID
    # ---------------------------------------------------------

    def get_by_id(
        self,
        instance_id
    ):

        return self.crud.get_by_id(
            self.model,
            instance_id
        )

    # ---------------------------------------------------------
    # DELETE
    # ---------------------------------------------------------

    def soft_delete(
        self,
        instance_id
    ):

        return self.crud.soft_delete(
            self.model,
            instance_id
        )

    # ---------------------------------------------------------
    # RESTORE
    # ---------------------------------------------------------

    def restore(
        self,
        instance_id
    ):

        return self.crud.restore(
            self.model,
            instance_id
        )

    # ---------------------------------------------------------
    # HARD DELETE
    # ---------------------------------------------------------

    def hard_delete(
        self,
        instance_id
    ):

        return self.crud.hard_delete(
            self.model,
            instance_id
        )


    # ---------------------------------------------------------
    # SEARCH
    # ---------------------------------------------------------

    def search(
        self,
        query_text,
        columns=None,
        include_inactive=False,
        filters=None
    ):

        return self.crud.search_columns(
            self.model,
            query_text,
            columns,
            include_inactive,
            filters
        )