from Model.parameter import Parameter #Parameter Modell importieren

#Dummy Daten
parameters = \
[
    Parameter(id=1, name="Glucose", unit="mg/dl", value=10.0),
    Parameter(id=2, name="Iron", unit="mg/dl", value=6.5),
    Parameter(id=3, name="CRP", unit="mg/dl", value=0.1),
]

#CRUD Funktionen
def get_parameters() -> list[Parameter]: #Alle Parameter zurückgeben
    return parameters

def get_parameter(name: str) -> Parameter | None: #Einen Parameter zurückgeben -> gemäss dem Namen
    for parameter in parameters:
        if parameter.name == name:
            return parameter
    return None

def create_parameter(parameter: Parameter) -> Parameter: #Einen Parameter erstellen
    return parameter

def update_parameter(parameter: Parameter) -> Parameter: #Einen Eintrag ändern
    return parameter

def replace_parameter(parameter: Parameter) -> Parameter: #Einen kompletten Parameter ersetzen
    return parameter

def delete_parameter(name: str) -> None: #Einen Parameter löschen
    return None  
