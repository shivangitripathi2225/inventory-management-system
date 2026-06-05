from sqlalchemy.orm import Session

from app.repositories.product_repository import (
    ProductRepository
)

from app.repositories.customer_repository import (
    CustomerRepository
)

from app.repositories.order_repository import (
    OrderRepository
)


class DashboardService:

    def __init__(self):
        self.product_repo = ProductRepository()
        self.customer_repo = CustomerRepository()
        self.order_repo = OrderRepository()

    def get_dashboard(
        self,
        db: Session
    ):

        return {
            "total_products":
                self.product_repo.count(db),

            "total_customers":
                self.customer_repo.count(db),

            "total_orders":
                self.order_repo.count(db),

            "low_stock_products":
                self.product_repo.count_low_stock(
                    db
                )
        }