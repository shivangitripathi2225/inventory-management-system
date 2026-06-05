from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.repositories.customer_repository import CustomerRepository

from app.core.exceptions import (
    CustomerNotFoundException,
    DuplicateCustomerEmailException
)


class CustomerService:

    def __init__(self):
        self.repo = CustomerRepository()

    def create_customer(
        self,
        db: Session,
        full_name: str,
        email: str,
        phone_number: str
    ):

        existing = self.repo.get_by_email(
            db,
            email
        )

        if existing:
            raise DuplicateCustomerEmailException()

        customer = Customer(
            full_name=full_name,
            email=email,
            phone_number=phone_number
        )

        try:
            created = self.repo.create(
                db,
                customer
            )

            db.commit()

            return created

        except Exception:
            db.rollback()
            raise

    def get_customer_by_id(
        self,
        db: Session,
        customer_id: int
    ):

        customer = self.repo.get_by_id(
            db,
            customer_id
        )

        if not customer:
            raise CustomerNotFoundException()

        return customer

    def get_customers(
        self,
        db: Session
    ):

        return self.repo.get_all(db)

    def delete_customer(
        self,
        db: Session,
        customer_id: int
    ):

        customer = self.repo.get_by_id(
            db,
            customer_id
        )

        if not customer:
            raise CustomerNotFoundException()

        try:
            self.repo.delete(
                db,
                customer
            )

            db.commit()

        except Exception:
            db.rollback()
            raise