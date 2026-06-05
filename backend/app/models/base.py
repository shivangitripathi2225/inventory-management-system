from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class TimestampMixin:
    created_at = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )