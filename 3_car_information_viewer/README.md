# Car Information Viewer

Basic FastAPI, Jinja, Bootstrap


[Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/.)

## pydantic
```python
class Car(BaseModel):
    make: str
    model: str
    year: int
    price: float
    engine: Optional[str] = "V4"
    autonomous: bool
    sold: List[str]
```
## Validation or field restrictions


[link](/3_car_information_viewer/note/field.md)

## Simulation database(python file)

Use a python file to simulate a database
使用 python file 來模擬資料庫

## Get all cars path(Query)

[link](/3_car_information_viewer/note/Get%20all%20cars%20path(Query).md)

## Get car by ID

[Path, HTTPException, status](/3_car_information_viewer/note/Path_HTTPException_status.md)

## Adding cars（Body）
利用HTTP POST的方法
可以利用下面的url來測試結果
```
http://127.0.0.1:8000/docs
```
