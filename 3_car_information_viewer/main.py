from fastapi import FastAPI, Query, Path, HTTPException, status, Body
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from database import cars

templates = Jinja2Templates(directory="templates")  # setting up HTML templates


class Car(BaseModel):
    make: Optional[str]
    model: Optional[str]
    year: Optional[int] = Field(..., ge=1970, lt=2022)
    price: Optional[float]
    engine: Optional[str] = "V4"
    autonomous: Optional[bool]
    sold: Optional[List[str]]


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")  # mounting the static files


@app.get("/")
def root():
    return {"hello"}


# http://127.0.0.1:8000/cars?number=2
@app.get("/cars", response_model=List[Dict[str, Car]])
def get_cars(number: Optional[str] = Query("10", max_length=3)):
    response = []
    for id, car in list(cars.items())[:int(number)]:
        to_add = {}
        to_add[id] = car
        response.append(to_add)
    return response


@app.get("/cars/{id}", response_model=Car)
def get_car_by_id(id: int = Path(..., ge=0, lt=1000)):
    car = cars.get(id)
    if not car:
        # raise HTTPException(status_code=404, detail="Couldn't find car by ID.")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Couldn't find car by ID.")
    return car


@app.post("/cars", status_code=status.HTTP_201_CREATED)
def add_cars(body_cars: List[Car], min_id: Optional[int] = Body(0)):
    if len(body_cars) < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No cars to add.")
    min_id = len(cars.values()) + min_id  # 獲取db的長度並加上偏移量
    for car in body_cars:
        while cars.get(min_id):  # 確保db不會被覆蓋，找到可用空間為止
            min_id += 1
        cars[min_id] = car
        min_id += 1


@app.put("/cars/{id}", response_model=Dict[str, Car])
def update_car(id: int, car: Car = Body(...)):
    stored = car.get(id)
    if not stored:  # 找不到此id(確保id的有效)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Could not find car with given ID.")
    stored = Car(**stored)  # 將字典解壓
    new = car.dict(exclude_unset=True)  # 不會利用初始值
    new = stored.copy(update=new)
    cars[id] = jsonable_encoder(new)
    response = {}
    response[id] = cars[id]
    return response


@app.delete("/cars/{id}")
def delete_car(id: int):
    if not cars.get(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Could not find car with given ID.")
    del cars[id]
