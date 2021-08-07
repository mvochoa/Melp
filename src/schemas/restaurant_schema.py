import re
from typing import Optional, Dict, Any
from fastapi import HTTPException, status
from fastapi.param_functions import Path
from pydantic import BaseModel, Field, validator
from pydantic.networks import AnyHttpUrl, EmailStr
from uuid import UUID

from .schema import ResponseModel


class RequestRestaurant(BaseModel):
    rating: int = Path(...,  gt=-1, le=4)
    name: str
    site: Optional[AnyHttpUrl] = Field(..., example="https://doma.in")
    email: Optional[EmailStr]
    phone: Optional[str] = Field(..., example="+00 (000) 0-00-00-00")
    street: Optional[str]
    city: Optional[str]
    state: Optional[str]
    lat: float = Field(..., example=-55.12467)
    lng: float = Field(..., example=12.67367)

    @validator('phone')
    def check_phone(cls, v):
        regex = "[-+(). \d]*"
        if re.search(regex, v):
            number = re.sub(r"[-+(). ]", "", v)
            if number.isnumeric() and len(number) >= 7 and len(number) <= 13:
                return v
        raise ValueError('Please provide a valid mobile phone number')


class ResponseRestaurant(ResponseModel, RequestRestaurant):
    id: UUID


class ResponseStatistics(ResponseModel):
    count: int
    avg: Optional[float]
    std: Optional[float]


class NotFoundRestaurantException(HTTPException):
    def __init__(self, id: str, headers: Optional[Dict[str, Any]] = {}) -> None:
        status_code = status.HTTP_404_NOT_FOUND
        detail = f"El restaurante con el ID '{id}' no se encontro"
        super().__init__(status_code, detail, headers)
