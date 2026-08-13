from pydantic import BaseModel

class Parameter(BaseModel): #Parameter Modell
    id: int #ID
    name: str #Name
    unit: str #Einheit
    value: float #Wert
