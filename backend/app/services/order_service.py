from decimal import Decimal

from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order import OrderItem

from app.repositories.order_repository import (
    OrderRepository
)
from collections import defaultdict
from app.repositories.customer_repository import (
    CustomerRepository
)

from app.repositories.product_repository import (
    ProductRepository
)

from app.schemas.order import OrderCreate

from app.core.exceptions import (
    CustomerNotFoundException,
    ProductNotFoundException,
    OrderNotFoundException,
    InsufficientInventoryException
)


class OrderService:

    def __init__(self):
        self.order_repo = OrderRepository()
        self.customer_repo = CustomerRepository()
        self.product_repo = ProductRepository()

    def create_order(
        self,
        db: Session,
        payload: OrderCreate
    ):

        customer = self.customer_repo.get_by_id(
            db,
            payload.customer_id
        )

        if not customer:
            raise CustomerNotFoundException()

        total_amount = Decimal("0.00")

        product_quantities = defaultdict(int)

        for item in payload.items:
            product_quantities[
                item.product_id
            ] += item.quantity

        validated_products = {}

        for product_id, quantity in product_quantities.items():

            product = self.product_repo.get_by_id(
                db,
                product_id
            )

            if not product:
                raise ProductNotFoundException()

            if product.quantity < quantity:
                raise InsufficientInventoryException(f"Insufficient stock for product {product.id}")

            validated_products[
                product_id
            ] = product

            total_amount += (
                product.price * quantity
            )

        try:

            order = Order(
                customer_id=payload.customer_id,
                total_amount=total_amount
            )

            order = self.order_repo.create(
                db,
                order
            )

            for item in payload.items:

                product = validated_products[
                    item.product_id
                ]

                order_item = OrderItem(
                    order_id=order.id,
                    product_id=product.id,
                    quantity=item.quantity,
                    unit_price=product.price
                )

                db.add(order_item)

                product.quantity -= item.quantity

            db.commit()

            db.refresh(order)

            return order

        except Exception:
            db.rollback()
            raise

    def get_order_by_id(
        self,
        db: Session,
        order_id: int
    ):

        order = self.order_repo.get_by_id(
            db,
            order_id
        )

        if not order:
            raise OrderNotFoundException()

        return order

    def get_orders(
        self,
        db: Session
    ):

        return self.order_repo.get_all(db)

    def delete_order(
        self,
        db: Session,
        order_id: int
    ):

        order = self.order_repo.get_by_id(
            db,
            order_id
        )

        if not order:
            raise OrderNotFoundException()

        try:

            self.order_repo.delete(
                db,
                order
            )

            db.commit()

        except Exception:
            db.rollback()
            raise