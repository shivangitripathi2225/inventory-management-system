from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    DuplicateSKUException,
    ProductNotFoundException
)
from app.core.exceptions import (
    CustomerNotFoundException,
    DuplicateCustomerEmailException,
    InsufficientInventoryException,
    OrderNotFoundException
)

def register_exception_handlers(app: FastAPI):

    @app.exception_handler(DuplicateSKUException)
    async def duplicate_sku_handler(
        request: Request,
        exc: DuplicateSKUException
    ):
        return JSONResponse(
            status_code=409,
            content={
                "detail": "SKU already exists"
            }
        )

    @app.exception_handler(ProductNotFoundException)
    async def product_not_found_handler(
        request: Request,
        exc: ProductNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail": "Product not found"
            }
        )
        
    @app.exception_handler(
        DuplicateCustomerEmailException
    )
    async def duplicate_customer_email_handler(
        request: Request,
        exc: DuplicateCustomerEmailException
    ):
        return JSONResponse(
            status_code=409,
            content={
                "detail": "Customer email already exists"
            }
        )


    @app.exception_handler(
        CustomerNotFoundException
    )
    async def customer_not_found_handler(
        request: Request,
        exc: CustomerNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail": "Customer not found"
            }
        )
    
    @app.exception_handler(InsufficientInventoryException)
    async def insufficient_inventory_handler(
        request: Request,
        exc: InsufficientInventoryException
    ):
        return JSONResponse(
            status_code=400,
            content={
                "detail": str(exc)
            }
        )
    
    @app.exception_handler(OrderNotFoundException)
    async def order_not_found_handler(
        request: Request,
        exc: OrderNotFoundException
    ):
        return JSONResponse(
            status_code=404,
            content={
                "detail": "Order not found"
            }
        )