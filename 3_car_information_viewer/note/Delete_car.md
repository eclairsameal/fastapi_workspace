## Delete car feature

car.html 裡追加 button
```html
    <a class="btn btn-danger" href="/delete/{{id}}">Delete</a>
```

再將delete改成post並改寫方法
```python
"""
@app.delete("/cars/{id}")
def delete_car(id: int):
    if not cars.get(id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Could not find car with given ID.")
    del cars[id]
"""


@app.get("/delete/{id}", response_class=RedirectResponse)
def delete_car(request: Request, id: int = Path(...)):
    if not cars.get(id):
        return templates.TemplateResponse("search.html", {"request": request, "id": id, "title": "Edit Car"}, status_code=status.HTTP_404_NOT_FOUND)
    del cars[id]
    return RedirectResponse(url="/cars")

```