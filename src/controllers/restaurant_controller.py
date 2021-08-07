from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from database.connection import get_db
from models.restaurant_model import RestaurantModel
from schemas.restaurant_schema import ResponseRestaurant, RequestRestaurant

router = APIRouter(
    prefix="/restaurants", tags=["Restaurantes"])


@router.post("", response_model=ResponseRestaurant, status_code=status.HTTP_201_CREATED, description="Registra nuevos restaurantes")
def create(request: RequestRestaurant, db: Session = Depends(get_db)):
    restaurant = RestaurantModel(**request.dict())
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant


@router.get("", response_model=List[ResponseRestaurant], description="Registra nuevos restaurantes")
def list(db: Session = Depends(get_db)):
    return db.query(RestaurantModel).all()
