from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate,
    ProductListResponse
)
from app.services.product_service import ProductService
from app.api.dependencies import get_product_service

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(
    payload: ProductCreate,
    db: Session = Depends(get_db),
    service: ProductService = Depends(get_product_service)
):
    return service.create_product(
        db=db,
        name=payload.name,
        sku=payload.sku,
        price=payload.price,
        quantity=payload.quantity
    )

from fastapi import Query

@router.get(
    "",
    response_model=ProductListResponse
)
def get_products(
    page: int = Query(default=1, ge=1),
    size: int = Query(default=10, ge=1, le=100),
    sku: str | None = None,
    search: str | None = None,
    db: Session = Depends(get_db),
    service: ProductService = Depends(get_product_service)
):
    return service.get_products(
        db=db,
        page=page,
        size=size,
        sku=sku,
        search=search
    )

@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    service: ProductService = Depends(get_product_service)
):
    return service.get_product_by_id(
        db,
        product_id
    )

from fastapi import Response


@router.delete(
    "/{product_id}",
    status_code=204
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    service: ProductService = Depends(get_product_service)
):

    service.delete_product(
        db,
        product_id
    )

    return Response(
        status_code=204
    )

@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: int,
    payload: ProductUpdate,
    db: Session = Depends(get_db),
    service: ProductService = Depends(get_product_service)
):
    return service.update_product(
        db,
        product_id,
        payload
    )