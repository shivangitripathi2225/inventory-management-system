from sqlalchemy.orm import Session

from app.models.order import Order, OrderItem


class OrderRepository:

    def create(
        self,
        db: Session,
        order: Order
    ) -> Order:

        db.add(order)
        db.flush()
        db.refresh(order)

        return order

    def get_by_id(
        self,
        db: Session,
        order_id: int
    ) -> Order | None:

        return (
            db.query(Order)
            .filter(Order.id == order_id)
            .first()
        )

    def get_all(
        self,
        db: Session
    ) -> list[Order]:

        return db.query(Order).all()
        
    def delete(
        self,
        db: Session,
        order: Order
    ):

        db.delete(order)

    def count(
        self,
        db: Session
    ) -> int:

        return db.query(Order).count()