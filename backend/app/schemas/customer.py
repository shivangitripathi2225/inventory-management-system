from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import ConfigDict


class CustomerCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone_number: str


class CustomerResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    full_name: str
    email: EmailStr
    phone_number: str