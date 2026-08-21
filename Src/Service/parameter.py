from Model.parameter import Parameter #Parameter Modell importieren
import Data.parameter as data #Datenbank-Layer importieren

#Middle Layer für die CRUD Operationen -> geben die Funktionen aus dem Data-Layer zurück
def get_parameters() -> list[Parameter]: #Alle Parameter zurückgeben -> Liste von Parametern
    return data.get_parameters() #Funktion-Call aus Data.parameter -> ohne Argument

def get_parameter(name: str) -> Parameter: #Einen Parameter zurückgeben -> gemäss dem Namen
    return data.get_parameter(name) #Funktion-Call aus Data.parameter -> mit Argument = Name des Parameters

def create_parameter(parameter: Parameter) -> Parameter: #Einen Parameter erstellen
    return data.create_parameter(parameter) #Funktion-Call aus Data.parameter -> mit Argument = Parameter-Modell

def update_parameter(name: str, parameter: Parameter) -> Parameter: #Einen Eintrag ändern
    return data.update_parameter(name, parameter) #Funktion-Call aus Data.parameter -> mit Argument = Name des Parameters und Parameter-Modell

def replace_parameter(name: str, parameter: Parameter) -> Parameter: #Einen kompletten Parameter ersetzen
    return data.replace_parameter(name, parameter) #Funktion-Call aus Data.parameter -> mit Argument = Name des Parameters und Parameter-Modell

def delete_parameter(name: str) -> None: #Einen Parameter löschen
    return data.delete_parameter(name) #Funktion-Call aus Data.parameter -> mit Argument = Name des Parameters
