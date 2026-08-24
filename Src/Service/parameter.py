from Model.parameter import Parameter, Create, Replace, Update #Modelle importieren
import Data.parameter as data #Datenbank-Layer importieren

#Middle Layer für die CRUD Operationen -> geben die Funktionen aus dem Data-Layer zurück
def get_parameters() -> list[Parameter]: #Alle Parameter zurückgeben -> Liste von Parametern
    return data.get_parameters() #Funktion-Call aus Data.parameter -> ohne Argument

def get_parameter(name: str) -> Parameter: #Einen Parameter zurückgeben -> gemäss dem Namen
    return data.get_parameter(name) #Funktion-Call aus Data.parameter -> mit Argument = Name des Parameters

def create_parameter(parameter: Create) -> Parameter: #Einen Parameter erstellen
    return data.create_parameter(parameter) #Funktion-Call aus Data.parameter -> mit Argument = Parameter-Modell

def update_parameter(name: str, new: Update) -> Parameter: #Einen Eintrag ändern
    current = data.get_parameter(name) #Aktueller Parameter
    updates = new.model_dump(exclude_unset=True) #Neuer Eintrag -> ohne ungesetzte Felder

    if "name" in updates and updates["name"] != name: #Kontrolle -> keine Name-Änderung
        raise ValueError("Name cannot be changed") #Fehlermeldung
    
    merged = current.model_copy(update=updates) #Aktueller Parameter mit dem neuen Eintrag verbinden
    return data.replace_parameter(name, merged) #Funktion-Call aus Data.parameter -> mit Argument = Name des Parameters und Parameter-Modell

def replace_parameter(name: str, new: Replace) -> Parameter: #Einen kompletten Parameter ersetzen
    if new.name != name: #Kontrolle -> Path-Parameter ist nicht identisch mit dem Body-Parameter
        raise ValueError(f"Path name '{name}' does not match body name '{new.name}'") #Fehlermeldung
    
    current = data.get_parameter(name) #Aktueller Parameter
    replaced = current.model_copy(update={"name": new.name, "unit": new.unit, "value": new.value}) #Neuer Parameter
    return data.replace_parameter(name, replaced) #Funktion-Call aus Data.parameter -> mit Argument = Name des Parameters und Parameter-Modell

def delete_parameter(name: str) -> None: #Einen Parameter löschen
    return data.delete_parameter(name) #Funktion-Call aus Data.parameter -> mit Argument = Name des Parameters
