# Adding a search feature
navber.html
```html
<form action="/search" method="POST" class="d-flex" style="margin: 0.5em;">
```
search.html
```html
{% include 'header.html' %}
{% include 'navber.html' %}
<div class="container">
    {% if car %}
        {% include 'car.html' %}
    {% else %}
        <h2>Oops! We couldn't find a car with that ID. Please try again.</h2>
    {% endif %}
</div>
{% include 'footer.html' %}
```
status_code=302:
如果我們不傳遞狀態代碼而它只是一個重定向，將會發生什麼是否會保留 Http post 方法。
所以這將發送一個 post 請求到 car slash ID，這是行不通的，因為我們不這樣做
main.py
```python
from fastapi import Form

@app.post("/search", response_class=RedirectResponse)
def search_cars(id: str = Form(...)):
    return RedirectResponse("/cars/" + id, status_code=302)


# @app.get("/cars/{id}", response_model=Car)
@app.get("/cars/{id}", response_class=HTMLResponse)
def get_car_by_id(request: Request, id: int = Path(..., ge=0, lt=1000)):
    car = cars.get(id)
    responde = templates.TemplateResponse("search.html", {"request": request, "car": car, "id": id,
                                                      "title": "Search Car"})
    if not car:
        # raise HTTPException(status_code=404, detail="Couldn't find car by ID.")
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Couldn't find car by ID.")
        # return templates.TemplateResponse("search.html", {"request": request, "car": car, "id": id,
        #                                                 "title": "Search Car"}, status_code=status.HTTP_404_NOT_FOUND)
        responde.status_code = status.HTTP_404_NOT_FOUND
    # return car
    return responde
```