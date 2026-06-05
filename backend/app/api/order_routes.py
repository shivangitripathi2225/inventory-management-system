from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.order import (
    OrderCreate,
    OrderResponse
)

from app.services.order_service import (
    OrderService
)

from app.api.dependencies import (
    get_order_service
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post(
    "",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED
)
def create_order(
    payload: OrderCreate,
    db: Session = Depends(get_db),
    service: OrderService = Depends(
        get_order_service
    )
):
    return service.create_order(
        db,
        payload
    )


@router.get(
    "",
    response_model=list[OrderResponse]
)
def get_orders(
    db: Session = Depends(get_db),
    service: OrderService = Depends(
        get_order_service
    )
):
    return service.get_orders(db)


@router.get(
    "/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db),
    service: OrderService = Depends(
        get_order_service
    )
):
    return service.get_order_by_id(
        db,
        order_id
    )


@router.delete(
    "/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    service: OrderService = Depends(
        get_order_service
    )
):

    service.delete_order(
        db,
        order_id
    )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )