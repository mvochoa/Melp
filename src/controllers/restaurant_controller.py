from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session

from database.connection import get_db
from models.restaurant_model import RestaurantModel
from schemas.schema import Detail
from schemas.restaurant_schema import ResponseRestaurant, RequestRestaurant

router = APIRouter(
    prefix="/restaurants", tags=["Restaurantes"])

responses_openapi = {404: {"model": Detail}}


@router.post("", response_model=ResponseRestaurant, status_code=status.HTTP_201_CREATED, description="Registra nuevos restaurantes")
def create(request: RequestRestaurant, db: Session = Depends(get_db)):
    restaurant = RestaurantModel(**request.dict())
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant


@router.get("", response_model=List[ResponseRestaurant], description="Lista los restaurantes registrados")
def list(db: Session = Depends(get_db)):
    return db.query(RestaurantModel).all()


@router.get("/{id}", response_model=ResponseRestaurant, responses=responses_openapi, description="Muestra los datos de un restaurante en especifico")
def show(id: str, db: Session = Depends(get_db)):
    restaurant = RestaurantModel.find(id, db)
    return restaurant.first()


@router.put("/{id}", response_model=ResponseRestaurant, responses=responses_openapi, description="Actualiza los datos de un restaurante en especifico")
def update(request: RequestRestaurant, id: str, db: Session = Depends(get_db)):
    restaurant = RestaurantModel.find(id, db)
    values = request.dict()
    values['site'] = str(values['site'])
    restaurant.update(values)
    return RestaurantModel.find(id, db).first()
