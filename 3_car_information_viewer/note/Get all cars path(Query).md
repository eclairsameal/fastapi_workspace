# Get all cars path(Query)

Returns all cars sent to the user in JSON format.

```python
@app.get("/cars", response_model=List[Dict[str, Car]])
def get_cars(number: Optional[str] = Query("10", max_length=3)):
```
number：是一個 Query Parameters
Query：基本上是另一個類似於字段和列表以及 DICT 的類，它允許我們指定查詢參數和函數。跟Field一樣第一個參數是預設值，後面的參數是各種限制。
max_length：限制不會超過999

### Run
Get all cars
```
http://127.0.0.1:8000/cars
```
```JSON
[
  {
    "1": {
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
  },
  {
    "2": {
      "make": "Speedy",
      "model": "FourWheeler SUV",
      "year": 2021,
      "price": 55400.0,
      "engine": "V4",
      "autonomous": false,
      "sold": [
        "AF",
        "AN",
        "AS",
        "EU",
        "NA",
        "OC",
        "SA"
      ]
    }
  },
  {
    "3": {
      "make": "Elektrik",
      "model": "AutoCar",
      "year": 2019,
      "price": 45000.0,
      "engine": "V8",
      "autonomous": true,
      "sold": [
        "AS"
      ]
    }
  },
  {
    "4": {
      "make": "CarBrand",
      "model": "Beetle",
      "year": 2004,
      "price": 21299.99,
      "engine": "V4",
      "autonomous": false,
      "sold": [
        
      ]
    }
  },
  {
    "5": {
      "make": "CarPro",
      "model": "Supersonic",
      "year": 2015,
      "price": 215000.0,
      "engine": "V12",
      "autonomous": false,
      "sold": [
        "NA",
        "AF",
        "OC",
        "SA"
      ]
    }
  }
]
```
取得2輛
```
http://127.0.0.1:8000/cars?number=2
```
```JSON
[
  {
    "1": {
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
  },
  {
    "2": {
      "make": "Speedy",
      "model": "FourWheeler SUV",
      "year": 2021,
      "price": 55400.0,
      "engine": "V4",
      "autonomous": false,
      "sold": [
        "AF",
        "AN",
        "AS",
        "EU",
        "NA",
        "OC",
        "SA"
      ]
    }
  }
]
```
參數超過範圍
```
http://127.0.0.1:8000/cars?number=1000
```
```JSON
{
  "detail": [
    {
      "loc": [
        "query",
        "number"
      ],
      "msg": "ensure this value has at most 3 characters",
      "type": "value_error.any_str.max_length",
      "ctx": {
        "limit_value": 3
      }
    }
  ]
}
```