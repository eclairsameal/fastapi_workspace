# Create car feature
我們已經有了實際創建汽車的後路由，但現在我們想將其轉換為適合的 HTML 格式。
所以我們要做到這一點的方法是有一個特殊的頁面，它將鏈接到 /create，正如我們在導航欄中描述的那樣。
這將有一個表單，它將一些數據發送到我們的post path，我們將擁有以與過去略有不同的方式對其進行管理，以使其真正發揮作用。

new create.html

main.py
```PYTHON
@app.get("/create", response_class=HTMLResponse)
def create_car(request: Request):
    return templates.TemplateResponse("create.html", {"request": request, "title": "Create Car"})
```

現在我們需要牢記的一件非常重要的事情是我們不再發送汽車清單或發送body data。

我們實際上是在發送表單數據。

所以我們這裡需要做的其實就是替換這個car的list，這個body cars的屬性或者參數

在這裡並將其替換為我們從表單中獲取的所有不同屬性。

現在，要記住的重要一點是它們是分開的。

他們不保持不變。

我們將需要為每個表單參數創建一個新參數。

main.py
```python
@app.post("/cars", status_code=status.HTTP_201_CREATED)
def add_cars(
        make: Optional[str] = Form(...),
        model: Optional[str] = Form(...),
        year: Optional[str] = Form(...),
        price: Optional[float] = Form(...),
        engine: Optional[str] = Form(...),
        autonomous: Optional[bool] = Form(...),
        sold: Optional[List[str]] = Form(None),
        min_id: Optional[int] = Body(0)):
    body_cars = [Car(make=make, model=model, year=year, price=price, engine=engine, autonomous=autonomous, sold=sold)]
    if len(body_cars) < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No cars to add.")
    min_id = len(cars.values()) + min_id  # 獲取db的長度並加上偏移量
    for car in body_cars:
        while cars.get(min_id):  # 確保db不會被覆蓋，找到可用空間為止
            min_id += 1
        cars[min_id] = car
        min_id += 1
    return RedirectResponse(url="/cars", status_code=302)
```