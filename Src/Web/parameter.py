from fastapi import APIRouter
from Model.parameter import Parameter #Parameter Modell importieren
import Service.parameter as service #Service Layer importieren

router = APIRouter(prefix = "/parameter") #Router erstellen -> Endpoint /parameter

@router.get("/") #Path Operation -> GET Request
def get_parameters() -> list[Parameter]: #Alle Parameter zurückgeben
    return service.get_parameters() #Funktion-Call aus Service.parameter -> ohne Argument

@router.get("/{name}") #Path Operation -> GET Request
def get_parameter(name: str) -> Parameter | None: #Einen Parameter zurückgeben -> gemäss dem Namen
    return service.get_parameter(name) #Funktion-Call aus Service.parameter -> mit Argument

@router.post("/") #Path Operation -> POST Request
def create_parameter(parameter: Parameter) -> Parameter: #Einen Parameter erstellen
    return service.create_parameter(parameter)

@router.patch("/") #Path Operation -> PATCH Request
def update_parameter(parameter: Parameter) -> Parameter: #Einen Eintrag ändern
    return service.update_parameter(parameter)

@router.put("/") #Path Operation -> PUT Request
def replace_parameter(parameter: Parameter) -> Parameter: #Einen kompletten Parameter ersetzen
    return service.replace_parameter(parameter)

@router.delete("/{name}") #Path Operation -> DELETE Request
def delete_parameter(name: str): #Einen Parameter löschen
    return service.delete_parameter(name) #Funktion-Call aus Service.parameter -> mit Argument
