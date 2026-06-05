from sqlalchemy import String
from sqlalchemy import Numeric
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import Base
from app.models.base import TimestampMixin


class Product(Base, TimestampMixin):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    sku: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )