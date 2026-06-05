from sqlalchemy.orm import Session

from app.models.customer import Customer


class CustomerRepository:

    def create(
        self,
        db: Session,
        customer: Customer
    ) -> Customer:

        db.add(customer)
        db.flush()
        db.refresh(customer)

        return customer

    def get_by_id(
        self,
        db: Session,
        customer_id: int
    ) -> Customer | None:

        return (
            db.query(Customer)
            .filter(Customer.id == customer_id)
            .first()
        )

    def get_by_email(
        self,
        db: Session,
        email: str
    ) -> Customer | None:

        return (
            db.query(Customer)
            .filter(Customer.email == email)
            .first()
        )

    def get_all(
        self,
        db: Session
    ) -> list[Customer]:

        return db.query(Customer).all()

    def delete(
        self,
        db: Session,
        customer: Customer
    ):
        db.delete(customer)

    def count(
        self,
        db: Session
    ) -> int:

        return db.query(Customer).count()