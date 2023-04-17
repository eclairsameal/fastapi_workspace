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
Using the HTTP POST method
利用HTTP POST的方法
You can use the following url to test the results
可以利用下面的url來測試結果
```
http://127.0.0.1:8000/docs
```

## Updating car

* 使用者可能只想修改一部分的資料，其他部分留白，可選變數可以讓這種狀況下也能執行
調整car Model 讓所有變數設定為可選
* 通過使用者給定的 ID 從我們的數據庫中獲取我們的想修改的汽車資料。

* 因為使用者只會輸入一部分的資料，我們希望沒輸入的部分為空值，而不是代入預設值
exclude_unset：除去預設值 
[官方文件](https://fastapi.tiangolo.com/zh/tutorial/body-updates/#pydantic-exclude_unset)

## Deleting car

基本跟 Get car by ID 一樣的寫法

