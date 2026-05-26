from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime
import datetime

Base = declarative_base()


class BaseMixin:

    id = Column(
        Integer,
        primary_key=True
    )

    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )