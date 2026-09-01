from fastapi import APIRouter, HTTPException
from Model.parameter import Parameter, Create, Update, Replace #Modelle importieren
from Service import parameter as service #Service Layer importieren
from Error.errors import MissingParameterError, DuplicateParameterError #Fehler Klassen importieren

router = APIRouter(prefix = "/parameter") #Router erstellen -> Endpoint /parameter

@router.get("") #Path Operation -> GET Request
def get_parameters() -> list[Parameter]: #Alle Parameter zurückgeben
    return service.get_parameters() #Funktion-Call aus Service.parameter -> ohne Argument

@router.get("/{name}") #Path Operation -> GET Request
def get_parameter(name: str) -> Parameter: #Einen Parameter zurückgeben
    try:
        return service.get_parameter(name) #Funktion-Call aus Service.parameter -> mit Argument = string name
    except MissingParameterError as error: #Ausnahme, falls der Parameter in der Datenbank nicht vorhanden ist
        raise HTTPException(status_code=404, detail=error.message) #Fehlermeldung -> 404 Not Found

@router.post("", status_code=201) #Path Operation -> POST Request / Status Code 201 -> Parameter erstellt
def create_parameter(parameter: Create) -> Parameter: #Einen Parameter erstellen
    try:
        return service.create_parameter(parameter) #Funktion-Call aus Service.parameter -> mit Argument = Create-Modell
    except DuplicateParameterError as error: #Ausnahme, falls der Parameter bereits in der Datenbank vorhanden ist
        raise HTTPException(status_code=409, detail=error.message) #Fehlermeldung -> 409 Conflict

@router.patch("/{name}") #Path Operation -> PATCH Request
def update_parameter(name: str, parameter: Update) -> Parameter: #Einen Eintrag ändern
    try:
        return service.update_parameter(name, parameter) #Funktion-Call aus Service.parameter -> mit Argument = Update-Modell / string name
    except MissingParameterError as error: #Ausnahme, falls der Parameter in der Datenbank nicht vorhanden ist
        raise HTTPException(status_code=404, detail=error.message) #Fehlermeldung -> 404 Not Found

@router.put("/{name}") #Path Operation -> PUT Request
def replace_parameter(name: str, parameter: Replace) -> Parameter: #Einen kompletten Parameter ersetzen
    try:
        return service.replace_parameter(name, parameter) #Funktion-Call aus Service.parameter -> mit Argument = Replace-Modell / string name
    except MissingParameterError as error: #Ausnahme, falls der Parameter in der Datenbank nicht vorhanden ist
        raise HTTPException(status_code=404, detail=error.message) #Fehlermeldung -> 404 Not Found
    except ValueError as error: #Ausnahme, falls der Parameter nicht ersetzt werden kann
        raise HTTPException(status_code=400, detail=str(error)) #Fehlermeldung -> 400 Bad Request

@router.delete("/{name}", status_code=204)#Path Operation -> DELETE Request / Status Code 204 -> Parameter gelöscht
def delete_parameter(name: str) -> None: #Einen Parameter löschen
    try:    
        return service.delete_parameter(name) #Funktion-Call aus Service.parameter -> mit Argument = string name
    except MissingParameterError as error: #Ausnahme, falls der Parameter in der Datenbank nicht vorhanden ist
        raise HTTPException(status_code=404, detail=error.message) #Fehlermeldung -> 404 Not Found
