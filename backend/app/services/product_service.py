from sqlalchemy.orm import Session
from decimal import Decimal
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductUpdate
from app.core.exceptions import (
    ProductNotFoundException,
    DuplicateSKUException
)


class ProductService:

    def __init__(self):
        self.repo = ProductRepository()


    def create_product(
        self,
        db: Session,
        name: str,
        sku: str,
        price: Decimal,
        quantity: int
    ):

        existing = self.repo.get_by_sku(
            db,
            sku
        )

        if existing:
            raise DuplicateSKUException()

        product = Product(
            name=name,
            sku=sku,
            price=price,
            quantity=quantity
        )
        try:
            created = self.repo.create(
                db,
                product
            )

            db.commit()

            return created
        except Exception:
            db.rollback()
            raise
    
    def get_product_by_id(
        self,
        db: Session,
        product_id: int
    ):

        product = self.repo.get_by_id(
            db,
            product_id
        )

        if not product:
            raise ProductNotFoundException()

        return product

    def get_products(
        self,
        db: Session,
        page: int,
        size: int,
        sku: str | None = None,
        search: str | None = None
    ):

        items, total = self.repo.get_products(
            db=db,
            page=page,
            size=size,
            sku=sku,
            search=search
        )

        return {
            "items": items,
            "page": page,
            "size": size,
            "total": total
        }

    def delete_product(
        self,
        db: Session,
        product_id: int
    ):

        product = self.repo.get_by_id(
            db,
            product_id
        )

        if not product:
            raise ProductNotFoundException()

        try:
            self.repo.delete(
                db,
                product
            )

            db.commit()

        except Exception:
            db.rollback()
            raise

    def update_product(
    self,
    db: Session,
    product_id: int,
    payload: ProductUpdate
    ):

        product = self.repo.get_by_id(
            db,
            product_id
        )

        if not product:
            raise ProductNotFoundException()

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                product,
                field,
                value
            )

        try:
            db.commit()
            db.refresh(product)

            return product

        except Exception:
            db.rollback()
            raise