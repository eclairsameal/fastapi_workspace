# Path, HTTPException, status

## Path
驗證路徑
```python
from fastapi import Path
@app.get("/cars/{id}", response_model=Car)
def get_car_by_id(id: int = Path(...,ge=0,lt=1000))
```
驗證路徑參數id的範圍要在0~1000內

## HTTPException
HTTP例外處理
```python
from fastapi import HTTPException
@app.get("/cars/{id}", response_model=Car)
def get_car_by_id(id: int = Path(..., ge=0, lt=1000)):
    car = cars.get(id)
    if not car:
        raise HTTPException(status_code=404, detail="Couldn't find car by ID.")
    return car
```

## status
這實際上只是存儲了那個數字 404，但它更容易一點，因為您實際上可以查看發生了什麼以及每個代碼的含義。

```python
from fastapi import HTTPException
@app.get("/cars/{id}", response_model=Car)
def get_car_by_id(id: int = Path(..., ge=0, lt=1000)):
    car = cars.get(id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Couldn't find car by ID.")
    return car
```

## run

```
http://127.0.0.1:8000/cars/1
```
```JSON
{
  "make": "CarBrand",
  "model": "Fast",
  "year": 1998,
  "price": 25000.0,
  "engine": "V8",
  "autonomous": false,
  "sold": [
    "NA",
    "EU"
  ]
}
```

```
http://127.0.0.1:8000/cars/200
```

```JSON
{
  "detail": "Couldn't find car by ID."
}
```