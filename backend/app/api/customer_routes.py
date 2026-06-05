from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Response

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse
)

from app.services.customer_service import CustomerService

from app.api.dependencies import (
    get_customer_service
)

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post(
    "",
    response_model=CustomerResponse,
    status_code=status.HTTP_201_CREATED
)
def create_customer(
    payload: CustomerCreate,
    db: Session = Depends(get_db),
    service: CustomerService = Depends(
        get_customer_service
    )
):
    return service.create_customer(
        db=db,
        full_name=payload.full_name,
        email=payload.email,
        phone_number=payload.phone_number
    )


@router.get(
    "",
    response_model=list[CustomerResponse]
)
def get_customers(
    db: Session = Depends(get_db),
    service: CustomerService = Depends(
        get_customer_service
    )
):
    return service.get_customers(db)


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse
)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db),
    service: CustomerService = Depends(
        get_customer_service
    )
):
    return service.get_customer_by_id(
        db,
        customer_id
    )


@router.delete(
    "/{customer_id}",
    status_code=204
)
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db),
    service: CustomerService = Depends(
        get_customer_service
    )
):

    service.delete_customer(
        db,
        customer_id
    )

    return Response(
        status_code=204
    )