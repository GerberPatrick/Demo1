from pydantic import BaseModel

class Parameter(BaseModel):
    id: int
    name: str
    unit: str
    value: float
