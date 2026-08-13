from fastapi import APIRouter
from Model.parameter import Parameter #Parameter Modell importieren
import Dummy.parameter as service #Dummy Daten importieren

router = APIRouter(prefix = "/parameter") #Router erstellen -> Endpoint /parameter

@router.get("/")
def get_parameters() -> list[Parameter]: #Alle Parameter zurückgeben
    return service.get_parameters()

@router.get("/{name}")
def get_parameter(name: str) -> Parameter | None: #Einen Parameter zurückgeben -> gemäss dem Namen
    return service.get_parameter(name)

@router.post("/")
def create_parameter(parameter: Parameter) -> Parameter: #Einen Parameter erstellen
    return service.create_parameter(parameter)

@router.patch("/")
def update_parameter(parameter: Parameter) -> Parameter: #Einen Eintrag ändern
    return service.update_parameter(parameter)

@router.put("/")
def replace_parameter(parameter: Parameter) -> Parameter: #Einen kompletten Parameter ersetzen
    return service.replace_parameter(parameter)

@router.delete("/{name}")
def delete_parameter(name: str): #Einen Parameter löschen
    return None
