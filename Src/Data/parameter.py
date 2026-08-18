from Data.init import connection, cursor, IntegrityError
from Error.errors import MissingParameterError, DuplicateParameterError
from Model.parameter import Parameter

cursor.execute("CREATE TABLE IF NOT EXISTS PARAMETER(id INTEGER PRIMARY KEY, name TEXT, unit TEXT, value REAL)") #Tabelle erstellen, falls nicht vorhanden

def row_to_model(row: tuple) -> Parameter: #Zeile in ein Model umwandeln
    id, name, unit, value = row #Zeile in ein Tuple umwandeln
    return Parameter(id=id, name=name, unit=unit, value=value) #Model erstellen

def model_to_dict(parameter: Parameter) -> dict: #Model in ein Dict umwandeln
    return parameter.dict()

def get_parameter(name: str) -> Parameter | None: #Einen Parameter aus der Datenbank auslesen
    query = "SELECT * FROM PARAMETER WHERE name=:name" #Query erstellen -> key:value Paar
    params = {"name": name} #Parameter erstellen
    cursor.execute(query, params) #Query ausführen
    row = cursor.fetchone() #Ergebnis auslesen -> Tuple
    if row:
        return row_to_model(row) #Zeile in ein Model umwandeln
    else:
        raise MissingParameterError(message=f"Parameter with name {name} not found") #Fehler, falls der Parameter in der Datenbank nicht gefunden wurde

def get_parameters() -> list[Parameter]: #Alle Parameter aus der Datenbank auslesen
    query = "SELECT * FROM PARAMETER" #Query erstellen
    cursor.execute(query) #Query ausführen
    rows = list(cursor.fetchall()) #Ergebnis auslesen
    return [row_to_model(row) for row in rows] #Alle Zeilen in ein Model umwandeln

def create_parameter(parameter: Parameter) -> Parameter | None: #Einen Parameter in die Datenbank einfügen
    if not parameter: 
        return None
    query = "INSERT INTO PARAMETER VALUES(:id, :name, :unit, :value)"
    params = model_to_dict(parameter) #Model Parameter in ein Dict umwandeln
    try:
        cursor.execute(query, params) #Query ausführen
    except IntegrityError:
        raise DuplicateParameterError(message=f"Parameter with name {parameter.name} already exists")
    connection.commit() #Änderungen speichern
    return get_parameter(parameter.name)

def update_parameter(name: str, parameter: Parameter) -> Parameter | None: #Einen Parameter in der Datenbank verändern
    if not (name and parameter): 
        return None
    query = "UPDATE PARAMETER SET name=:name, unit=:unit, value=:value WHERE name=:name_original"
    params = model_to_dict(parameter) #Model Parameter in ein Dict umwandeln
    params["name_original"] = parameter.name #Original Name in das Dict hinzufügen
    cursor.execute(query, params) #Query ausführen
    if cursor.rowcount == 1:
        connection.commit() #Änderungen speichern
        return get_parameter(parameter.name)
    else:
        raise MissingParameterError(message=f"Parameter with name {parameter.name} not found")

def replace_parameter(name: str, parameter: Parameter) -> Parameter | None: #Einen Parameter in der Datenbank ersetzen
    if not (name and parameter): 
        return None
    query = "UPDATE PARAMETER SET name=:name, unit=:unit, value=:value WHERE name=:name_original"
    params = model_to_dict(parameter) #Model Parameter in ein Dict umwandeln
    params["name_original"] = parameter.name #Original Name in das Dict hinzufügen
    cursor.execute(query, params) #Query ausführen
    if cursor.rowcount == 1:
        connection.commit() #Änderungen speichern
        return get_parameter(parameter.name)
    else:
        raise MissingParameterError(message=f"Parameter with name {parameter.name} not found")

def delete_parameter(name: str) -> bool: #Einen Parameter in der Datenbank löschen
    if not name: 
        return False
    query = "DELETE FROM PARAMETER WHERE name=:name" #Query erstellen -> key:value Paar
    params = {"name": name} #Parameter erstellen
    cursor.execute(query, params) #Query ausführen
    if cursor.rowcount != 1:
        raise MissingParameterError(message=f"Parameter with name {name} not found")
