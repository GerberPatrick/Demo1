from init import connection, cursor
from Model.parameter import Parameter

cursor.execute("CREATE TABLE IF NOT EXISTS PARAMETER(id INTEGER PRIMARY KEY, name TEXT, unit TEXT, value REAL)") #Tabelle erstellen, falls nicht vorhanden

def row_to_model(row: tuple) -> Parameter: #Zeile in ein Model umwandeln
    id, name, unit, value = row #Zeile in ein Tuple umwandeln
    return Parameter(id, name, unit, value) #Model erstellen

def model_to_dict(parameter: Parameter) -> dict: #Model in ein Dict umwandeln
    return parameter.dict()

def get_parameter(name: str) -> Parameter | None: #Einen Parameter aus der Datenbank auslesen
    query = "SELECT * FROM PARAMETER WHERE name=:name" #Query erstellen -> key:value Paar
    params = {"name": name} #Parameter erstellen
    cursor.execute(query, params) #Query ausführen
    row = cursor.fetchone() #Ergebnis auslesen -> Tuple

    if row:
        return row_to_model(row) #Zeile in ein Model umwandeln
    return None

def get_parameters() -> list[Parameter]: #Alle Parameter aus der Datenbank auslesen
    query = "SELECT * FROM PARAMETER" #Query erstellen
    cursor.execute(query) #Query ausführen
    rows = list(cursor.fetchall()) #Ergebnis auslesen
    return [row_to_model(row) for row in rows] #Alle Zeilen in ein Model umwandeln

def create_parameter(parameter: Parameter) -> Parameter: #Einen Parameter in die Datenbank einfügen
    query = "INSERT INTO PARAMETER VALUES(:id, :name, :unit, :value)"
    params = model_to_dict(parameter) #Model Parameter in ein Dict umwandeln
    cursor.execute(query, params) #Query ausführen
    connection.commit() #Änderungen speichern
    return get_parameter(parameter.name)

def update_parameter(parameter: Parameter) -> Parameter: #Einen Parameter in der Datenbank verändern
    query = "UPDATE PARAMETER SET name=:name, unit=:unit, value=:value WHERE name=:name_original"
    params = model_to_dict(parameter) #Model Parameter in ein Dict umwandeln
    params["name_original"] = parameter.name #Original Name in das Dict hinzufügen
    cursor.execute(query, params) #Query ausführen
    connection.commit() #Änderungen speichern
    return get_parameter(parameter.name)

def replace_parameter(parameter: Parameter) -> Parameter: #Einen Parameter in der Datenbank ersetzen
    query = "UPDATE PARAMETER SET name=:name, unit=:unit, value=:value WHERE name=:name_original"
    params = model_to_dict(parameter) #Model Parameter in ein Dict umwandeln
    params["name_original"] = parameter.name #Original Name in das Dict hinzufügen
    cursor.execute(query, params) #Query ausführen
    connection.commit() #Änderungen speichern
    return get_parameter(parameter.name)

def delete_parameter(parameter: Parameter) -> bool: #Einen Parameter in der Datenbank löschen
    query = "DELETE FROM PARAMETER WHERE name=:name" #Query erstellen -> key:value Paar
    params = {"name": parameter.name} #Parameter erstellen
    result = cursor.execute(query, params) #Query ausführen
    connection.commit() #Änderungen speichern
    return bool(result) #True wenn der Parameter gelöscht wurde, False wenn nicht
