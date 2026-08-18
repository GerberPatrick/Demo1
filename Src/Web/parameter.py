from fastapi import APIRouter, HTTPException
from Model.parameter import Parameter #Parameter Modell importieren
from Service import parameter as service #Service Layer importieren
from Error.errors import MissingParameterError, DuplicateParameterError #Fehler Klassen importieren

router = APIRouter(prefix = "/parameter") #Router erstellen -> Endpoint /parameter bzw. /parameter/

@router.get("") #Path Operation -> GET Request
@router.get("/") #Path Operation -> GET Request
def get_parameters() -> list[Parameter]: #Alle Parameter zurückgeben
    return service.get_parameters() #Funktion-Call aus Service.parameter -> ohne Argument

@router.get("/{name}") #Path Operation -> GET Request
def get_parameter(name: str) -> Parameter | None: #Einen Parameter zurückgeben -> gemäss dem Namen
    try:
        return service.get_parameter(name) #Funktion-Call aus Service.parameter -> mit Argument
    except MissingParameterError as e: 
        raise HTTPException(status_code=404, detail=e.message) #Fehler, falls der Parameter in der Datenbank nicht gefunden wurde

@router.post("", status_code=201) #Path Operation -> POST Request / Status Code 201 -> Parameter erstellt
@router.post("/", status_code=201) #Path Operation -> POST Request / Status Code 201 -> Parameter erstellt
def create_parameter(parameter: Parameter) -> Parameter: #Einen Parameter erstellen
    try:
        return service.create_parameter(parameter) #Funktion-Call aus Service.parameter -> mit Argument
    except DuplicateParameterError as e:
        raise HTTPException(status_code=404, detail=e.message) #Fehler, falls der Parameter nicht erstellt werden konnte

@router.patch("") #Path Operation -> PATCH Request
@router.patch("/") #Path Operation -> PATCH Request
def update_parameter(name: str, parameter: Parameter) -> Parameter: #Einen Eintrag ändern
    try:
        return service.update_parameter(name, parameter) #Funktion-Call aus Service.parameter -> mit Argument
    except MissingParameterError as e:
        raise HTTPException(status_code=404, detail=e.message) #Fehler, falls der Parameter nicht gefunden wurde

@router.put("") #Path Operation -> PUT Request
@router.put("/") #Path Operation -> PUT Request
def replace_parameter(name: str, parameter: Parameter) -> Parameter: #Einen kompletten Parameter ersetzen
    try:
        return service.replace_parameter(name, parameter) #Funktion-Call aus Service.parameter -> mit Argument
    except MissingParameterError as e:
        raise HTTPException(status_code=404, detail=e.message) #Fehler, falls der Parameter nicht gefunden wurde

@router.delete("/{name}", status_code=204)#Path Operation -> DELETE Request / Status Code 204 -> Parameter gelöscht
def delete_parameter(name: str) -> None: #Einen Parameter löschen
    try:    
        return service.delete_parameter(name) #Funktion-Call aus Service.parameter -> mit Argument
    except MissingParameterError as e:
        raise HTTPException(status_code=404, detail=e.message) #Fehler, falls der Parameter nicht gefunden wurde
