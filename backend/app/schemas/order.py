from decimal import Decimal
from pydantic import BaseModel
from pydantic import Field
from pydantic import ConfigDict


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)


class OrderCreate(BaseModel):
    customer_id: int
    items: list[OrderItemCreate] = Field(
        min_length=1
    )


class OrderItemResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    product_id: int
    quantity: int
    unit_price: Decimal


class OrderResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    customer_id: int
    total_amount: Decimal
    items: list[OrderItemResponse] = []