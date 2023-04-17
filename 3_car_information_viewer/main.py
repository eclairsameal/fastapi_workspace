from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from database import cars

class Car(BaseModel):
    make: str
    model: str
    year: int = Field(..., ge=1970, lt=2022)  # 1970 >= year >= 2022
    price: float
    engine: Optional[str] = "V4"
    autonomous: bool
    sold: List[str]


app = FastAPI()

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
