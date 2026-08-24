from pydantic import BaseModel, Field, model_validator

class Parameter(BaseModel): #Parameter-Modell
    id: int #ID
    name: str #Name
    unit: str #Einheit
    value: float #Wert

class Create(BaseModel): #Create-Modell -> alle Felder müssen gesetzt werden -> Validation
    name: str = Field(min_length=1, max_length=100) #Name
    unit: str = Field(min_length=1, max_length=100) #Einheit
    value: float #Wert

class Replace(BaseModel): #Replace-Modell -> alle Felder müssen gesetzt werden -> Validation
    name: str = Field(min_length=1, max_length=100) #Name
    unit: str = Field(min_length=1, max_length=100) #Einheit
    value: float #Wert

class Update(BaseModel): #Update-Modell -> Jedes Feld ist optional / ein Feld muss gesetzt werden -> Validation
    name: str | None = Field(default=None, min_length=1, max_length=100) #Name
    unit: str | None = Field(default=None, min_length=1, max_length=100) #Einheit
    value: float | None = None #Wert

    @model_validator(mode="after")
    def one_field(self):
        if self.name is None and self.unit is None and self.value is None:
            raise ValueError("One field must be set")
        return self
