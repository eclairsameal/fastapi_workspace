# Creating your first HTML response

## import
```python
from fastapi import Request
```
## 將請求作為參數或參數包含在我們的根函數
Include the request as a parameter or parameter in our root function
```python
@app.get("/")
def root(request: Request):
    # return {"hello"}
    return templates.TemplateResponse("home.html", {"request": request})
```
templates：剛剛宣告的templates變數
TemplateResponse：
    參數1：html 模板名稱
    參數2：dict, 想要傳遞的一些值和變量(需要將請求傳遞給每個 HTML 響應)

## 指定我們想要的響應類型

```python
from starlette.responses import HTMLResponse
@app.get("/", response_class=HTMLResponse)
```

## 傳遞參數並顯示
main.py
```python
return templates.TemplateResponse("home.html",
                                      {"request": request, "title": "FastAPI Home",
                                       "text": "Welcome to your frist app in FastAPI"})
```
home.html
```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}}</title>
</head>
<body>
    <h1>{{text}}</h1>
    
</body>
</html>

```