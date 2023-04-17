# Validation or field restrictions

Add some additional constraints(額外的限制) to pydantic models

[body-fields](https://fastapi.tiangolo.com/tutorial/body-fields/)

```python
from pydantic import Field

variable_name: data_type = (default, various constraints)
```
當default不是必須時：...

### Example
Let's say I want to shorten the year. I don't want any cars older than 1970 or later than the latest models.
假設我想縮短年份。我不想要任何早於 1970 年或晚於最新款的汽車。

```python
from pydantic import Field
class Car(BaseModel):
    make: str
    model: str
    year: int = Field(..., ge=1970, lt=2022)  # 1970 >= year >= 2022
    price: float
    engine: Optional[str] = "V4"
    autonomous: bool
    sold: List[str]
```