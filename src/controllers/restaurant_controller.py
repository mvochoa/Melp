from typing import List
from fastapi import APIRouter, status
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from sqlalchemy.sql import func

from database.connection import get_db
from models.restaurant_model import RestaurantModel
from schemas.schema import Detail
from schemas.restaurant_schema import ResponseRestaurant, RequestRestaurant, ResponseStatistics

router = APIRouter(
    prefix="/restaurants", tags=["Restaurantes"])

responses_openapi = {404: {"model": Detail}}


@router.get("/statistics", response_model=ResponseStatistics, description="Muestra estadisiticas de restaurantes dentro de un circulo de cierto radio (metros) con el centro en una latitud y longitud especifica")
def list(latitude: float, longitude: float, radius: float, db: Session = Depends(get_db)):
    return db.query(func.count(RestaurantModel.id).label('count'), func.avg(RestaurantModel.rating).label('avg'), func.stddev(RestaurantModel.rating).label('std'),).filter(func.ST_DistanceSphere(func.ST_MakePoint(
        RestaurantModel.lng, RestaurantModel.lat), func.ST_MakePoint(longitude, latitude)) <= radius).first()


@router.get("", response_model=List[ResponseRestaurant], description="Lista los restaurantes registrados")
def list(db: Session = Depends(get_db)):
    return db.query(RestaurantModel).all()


@router.get("/{id}", response_model=ResponseRestaurant, responses=responses_openapi, description="Muestra los datos de un restaurante en especifico")
def show(id: str, db: Session = Depends(get_db)):
    restaurant = RestaurantModel.find(id, db)
    return restaurant.first()


@router.post("", response_model=ResponseRestaurant, status_code=status.HTTP_201_CREATED, description="Registra nuevos restaurantes")
def create(request: RequestRestaurant, db: Session = Depends(get_db)):
    restaurant = RestaurantModel(**request.dict())
    db.add(restaurant)
    db.commit()
    db.refresh(restaurant)
    return restaurant


@router.put("/{id}", response_model=ResponseRestaurant, responses=responses_openapi, description="Actualiza los datos de un restaurante en especifico")
def update(request: RequestRestaurant, id: str, db: Session = Depends(get_db)):
    restaurant = RestaurantModel.find(id, db)
    values = request.dict()
    values['site'] = str(values['site'])
    restaurant.update(values)
    db.commit()
    return RestaurantModel.find(id, db).first()


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, responses=responses_openapi, description="Elimina un restaurante en especifico")
def destroy(id: str, db: Session = Depends(get_db)):
    restaurant = RestaurantModel.find(id, db)
    restaurant.delete()
    db.commit()
