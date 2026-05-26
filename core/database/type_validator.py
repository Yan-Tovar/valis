from datetime import (
    date,
    datetime
)

from decimal import Decimal

from sqlalchemy.inspection import inspect

from sqlalchemy.sql.sqltypes import (

    Integer,

    Float,

    String,

    Text,

    Date,

    DateTime,

    Boolean,

    Numeric,

    Enum
)

from core.database.exceptions import (
    ValidationError
)


class TypeValidator:


    @staticmethod
    def validate(
        model,
        data
    ):

        mapper = inspect(model)

        for column in mapper.columns:

            # -------------------------------------------------
            # VALUE
            # -------------------------------------------------

            value = data.get(column.name)

            if value is None:
                continue

            # -------------------------------------------------
            # COLUMN TYPE
            # -------------------------------------------------

            column_type = column.type

            # -------------------------------------------------
            # INTEGER
            # -------------------------------------------------

            if isinstance(column_type, Integer):

                if not isinstance(value, int):

                    raise ValidationError(
                        f"'{column.name}' debe ser entero"
                    )

            # -------------------------------------------------
            # FLOAT
            # -------------------------------------------------

            elif isinstance(column_type, Float):

                if not isinstance(
                    value,
                    (int, float)
                ):

                    raise ValidationError(
                        f"'{column.name}' debe ser numérico"
                    )

            # -------------------------------------------------
            # NUMERIC / DECIMAL
            # -------------------------------------------------

            elif isinstance(column_type, Numeric):

                if not isinstance(
                    value,
                    (
                        int,
                        float,
                        Decimal
                    )
                ):

                    raise ValidationError(
                        f"'{column.name}' debe ser decimal"
                    )

            # -------------------------------------------------
            # STRING
            # -------------------------------------------------

            elif isinstance(
                column_type,
                (
                    String,
                    Text
                )
            ):

                if not isinstance(value, str):

                    raise ValidationError(
                        f"'{column.name}' debe ser texto"
                    )

            # -------------------------------------------------
            # BOOLEAN
            # -------------------------------------------------

            elif isinstance(column_type, Boolean):

                if not isinstance(value, bool):

                    raise ValidationError(
                        f"'{column.name}' debe ser booleano"
                    )

            # -------------------------------------------------
            # DATE
            # -------------------------------------------------

            elif isinstance(column_type, Date):

                if not isinstance(
                    value,
                    date
                ):

                    raise ValidationError(
                        f"'{column.name}' debe ser fecha"
                    )

            # -------------------------------------------------
            # DATETIME
            # -------------------------------------------------

            elif isinstance(
                column_type,
                DateTime
            ):

                if not isinstance(
                    value,
                    datetime
                ):

                    raise ValidationError(
                        f"'{column.name}' debe ser fecha y hora"
                    )

            # -------------------------------------------------
            # ENUM
            # -------------------------------------------------

            elif isinstance(column_type, Enum):

                valid_values = (
                    column_type.enums
                )

                if value not in valid_values:

                    raise ValidationError(

                        f"'{column.name}' debe ser uno de: "
                        f"{', '.join(valid_values)}"
                    )