from fastapi import FastAPI
from app.api.product_routes import router as product_router
from app.core.exception_handlers import register_exception_handlers
from app.middleware.request_logging import (
    RequestLoggingMiddleware
)
from app.api.customer_routes import (
    router as customer_router
)
from app.api.order_routes import (
    router as order_router
)
from app.api.dashboard_routes import (
    router as dashboard_router
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = "Inventory Management System", version="1.0.0")

register_exception_handlers(app)
app.add_middleware(
    RequestLoggingMiddleware
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)
app.include_router(customer_router)
app.include_router(order_router)
app.include_router(dashboard_router)

@app.get("/")
def health():
    return {"status": "healthy"}