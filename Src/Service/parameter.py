from Model.parameter import Parameter #Parameter Modell importieren
import Data.parameter as data #Datenbank-Layer importieren

#Middle Layer für die CRUD Operationen
def get_parameters() -> list[Parameter]: #Alle Parameter zurückgeben
    return data.get_parameters()

def get_parameter(name: str) -> Parameter | None: #Einen Parameter zurückgeben -> gemäss dem Namen
    return data.get_parameter(name)

def create_parameter(parameter: Parameter) -> Parameter: #Einen Parameter erstellen
    return data.create_parameter(parameter)

def update_parameter(name: str, parameter: Parameter) -> Parameter: #Einen Eintrag ändern
    return data.update_parameter(name, parameter)

def replace_parameter(name: str, parameter: Parameter) -> Parameter: #Einen kompletten Parameter ersetzen
    return data.replace_parameter(name, parameter)

def delete_parameter(name: str) -> None: #Einen Parameter löschen
    return data.delete_parameter(name)
