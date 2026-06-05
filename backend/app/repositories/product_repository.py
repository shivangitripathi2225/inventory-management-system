# app/repositories/product_repository.py

from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    def create(
        self,
        db: Session,
        product: Product
    ) -> Product:

        db.add(product)
        db.flush()
        db.refresh(product)

        return product


    def get_by_id(
        self,
        db: Session,
        product_id: int
    ) -> Product | None:

        return (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )


    def get_by_sku(
        self,
        db: Session,
        sku: str
    ) -> Product | None:

        return (
            db.query(Product)
            .filter(Product.sku == sku)
            .first()
        )


    def get_all(
        self,
        db: Session
    ) -> list[Product]:

        return db.query(Product).all()


    def delete(
        self,
        db: Session,
        product: Product
    ):

        db.delete(product)


    def get_products(
        self,
        db: Session,
        page: int,
        size: int,
        sku: str | None = None,
        search: str | None = None
    ):
        query = db.query(Product)

        if sku:
            query = query.filter(
                Product.sku == sku
            )

        if search:
            query = query.filter(
                Product.name.ilike(
                    f"%{search}%"
                )
            )

        total = query.count()

        items = (
            query
        .order_by(Product.id)
        .offset((page - 1) * size)
        .limit(size)
        .all()
    )
        return items, total
    
    def count(
        self,
        db: Session
    ) -> int:

        return db.query(Product).count()


    def count_low_stock(
        self,
        db: Session,
        threshold: int = 5
    ) -> int:

        return (
            db.query(Product)
            .filter(Product.quantity <= threshold)
            .count()
        )