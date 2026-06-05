from decimal import Decimal

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class ProductCreate(BaseModel):
    name: str
    sku: str
    price: Decimal
    quantity: int = Field(ge=0)


class ProductUpdate(BaseModel):
    name: str | None = None
    price: Decimal | None = None
    quantity: int | None = Field(
        default=None,
        ge=0
    )


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    sku: str
    price: Decimal
    quantity: int


class ProductListResponse(BaseModel):
    items: list[ProductResponse]
    page: int
    size: int
    total: int