# Edit car feature

car.html 裡追加 button
```html
    <a class="btn btn-dark" href="/edit?id={{id}}">Edit</a>
```

追加get 方法
main.py
```python
@app.get("/edit", response_class=HTMLResponse)
def edit_car(request: Request, id: int = Query(...)):
    car = cars.get(id)
    if not car:
        return templates.TemplateResponse("search.html", {"request": request, "id": id, "car": car, "title": "Edit Car"}
                                          , status_code=status.HTTP_404_NOT_FOUND)
    return templates.TemplateResponse("edit.html", {"request": request, "id": id, "car": car, "title": "Edit Car"})
```

edit.html -> copy create.html 再做修改

```html

<input value="{{car['make']}}">

<select class="form-select" name="autonomous" id="autonomous">
    {% if car['autonomous'] %}
        <option selected value="true">Yes</option>
        <option value="false">No</option>
    {% else %}
        <option  value="true">Yes</option>
        <option selected value="false">No</option>
    {% endif %}
</select>

<p>Where is the car sold?</p>
<div class="form-check">
    {% for ct in [("Africa", "AF"), ("Antarctica", "AN"), ("Asia", "AS"), ("Europe", "EU"), ("North America", "NA"),
    ("Oceania", "OC"), ("South America", "SA")]%}
    {% if ct[1] in car['sold']%}
        <input class="form-check-input" type="checkbox" value="{{ct[1]}}" name="sold" checked>{{ct[0]}} ({{ct[1]}})<br>
    {% else %}
        <input class="form-check-input" type="checkbox" value="{{ct[1]}}" name="sold">{{ct[0]}} ({{ct[1]}})<br>
    {% endif %}
    {% endfor %}
</div>
```

不幸的是，html表單不支持put和delete操作。
```html
<form action="/cars/{{id}}" method="POST">
```
再將put改成post並改寫方法
```python
"""
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
"""


@app.post("/cars/{id}")
def update_car(request: Request, id: int,
    make: Optional[str] = Form(None),
    model: Optional[str] = Form(None),
    year: Optional[str] = Form(None),
    price: Optional[float] = Form(None),
    engine: Optional[str] = Form(None),
    autonomous: Optional[bool] = Form(None),
    sold: Optional[List[str]] = Form(None),):
    stored = cars.get(id)
    if not stored:
        return templates.TemplateResponse("search.html",
                                          {"request": request, "id": id, "car": stored, "title": "Edit Car"},
                                          status_code=status.HTTP_404_NOT_FOUND)
    stored = Car(**dict(stored))  # 確保它是字典格式再解壓
    # 改變成用 pydantic 型態的 car 變數
    car = Car(make=make, model=model, year=year, price=price, engine=engine, autonomous=autonomous, sold=sold)
    new = car.dict(exclude_unset=True)
    new = stored.copy(update=new)
    cars[id] = jsonable_encoder(new)
    response = {}
    response[id] = cars[id]
    return RedirectResponse(url="/cars", status_code=302)

```