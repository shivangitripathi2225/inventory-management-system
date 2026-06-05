from app.services.product_service import ProductService
from app.services.customer_service import CustomerService
from app.services.order_service import OrderService
from app.services.dashboard_service import (
    DashboardService
)

def get_product_service():
    return ProductService()


def get_customer_service():
    return CustomerService()


def get_order_service():
    return OrderService()

def get_dashboard_service():
    return DashboardService()