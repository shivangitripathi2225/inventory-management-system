from sqlalchemy.orm import mapped_column
from app.models.base import Base, TimestampMixin
from sqlalchemy import Integer, ForeignKey, Numeric
from sqlalchemy.orm import relationship
class Order(Base, TimestampMixin):
    __tablename__ = "orders"

    id = mapped_column(Integer, primary_key=True)

    customer_id = mapped_column(
        ForeignKey("customers.id"),
        nullable=False
    )

    total_amount = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan"
    )


class OrderItem(Base):

    __tablename__ = "order_items"

    id = mapped_column(Integer, primary_key=True)

    order_id = mapped_column(
        ForeignKey("orders.id"),
        nullable=False
    )

    product_id = mapped_column(
        ForeignKey("products.id"),
        nullable=False
    )

    quantity = mapped_column(
        Integer,
        nullable=False
    )

    unit_price = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    order = relationship(
        "Order",
        back_populates="items"
    )