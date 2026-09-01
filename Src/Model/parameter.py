from pydantic import BaseModel, Field, model_validator, ConfigDict

class Parameter(BaseModel): #Parameter-Modell
    id: int 
    name: str 
    unit: str 
    value: float 

class Create(BaseModel): #Create-Modell -> alle Felder müssen gesetzt werden -> Validation
    name: str = Field(min_length=1, max_length=100) 
    unit: str = Field(min_length=1, max_length=100) 
    value: float 

class Replace(BaseModel): #Replace-Modell -> alle Felder müssen gesetzt werden -> Validation
    name: str = Field(min_length=1, max_length=100) 
    unit: str = Field(min_length=1, max_length=100) 
    value: float 

class Update(BaseModel): #Update-Modell -> Nur Felder unit und value können gesetzt werden / name bleibt im Pfad -> Validation
    model_config = ConfigDict(extra="forbid")
    unit: str | None = Field(default=None, min_length=1, max_length=100) 
    value: float | None = None 

    @model_validator(mode="after")
    def one_field(self):
        if self.unit is None and self.value is None:
            raise ValueError("One field must be set")
        return self
