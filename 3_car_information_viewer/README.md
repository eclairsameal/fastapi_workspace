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

Test Results :
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

Basically the same as Get car by ID
基本跟 Get car by ID 一樣的寫法

**到此 REST API 已經完成**

## setting up HTML templates
Jinja2 : Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax.

The way Jinja works is it has a specific directory called templates, and this is going to contain all of your HTML that you need

1. new templates folder
   new static folder
2. import
```python
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
```
3. create a templates variable 
   Allows us to return a templated response populated with all the data we need, which will work with Jinja.
   允許我們返回模板響應並填充在我們需要的所有數據中，這將與 Jinja 一起工作。
```python
templates = Jinja2Templates(directory="templates")
```
4. mounting the static files
   放到app中來被使用
   ```python
   app.mount("/static", StaticFiles(directory="static"), name="static")
   # 路徑 型態 名稱
   ```
 
 ## Creating your first HTML response
創建一個html回應並應用模板來顯示傳遞的參數
[HTML response](/3_car_information_viewer/note/HTML_response.md)

##  Header & footer components
導入 Bootstrap
創建通用樣板(所有頁面都一樣的部分)


