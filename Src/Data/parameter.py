from Data.init import connection, cursor, IntegrityError #Datenbank-Layer importieren -> zwei Instanzen: connection und cursor
from Error.errors import MissingParameterError, DuplicateParameterError #Fehler-Layer importieren -> zwei Klassen: MissingParameterError und DuplicateParameterError
from Model.parameter import Parameter #Model-Layer importieren -> Klasse: Parameter

cursor.execute("CREATE TABLE IF NOT EXISTS PARAMETER(id INTEGER PRIMARY KEY, name UNIQUE, unit TEXT, value REAL)") #Tabelle erstellen, falls nicht vorhanden

def row_to_model(row: tuple) -> Parameter: #Zeile in ein Model umwandeln -> Tuple aus id, name, unit und value
    id, name, unit, value = row #Zeile in ein Tuple umwandeln
    return Parameter(id=id, name=name, unit=unit, value=value) #Model erstellen

def model_to_dict(parameter: Parameter) -> dict: #Model in ein Dict umwandeln
    return parameter.dict()

def get_parameter(name: str) -> Parameter: #Einen Parameter aus der Datenbank auslesen -> gemäss dem Namen
    query = "SELECT * FROM PARAMETER WHERE name=:name" #Query erstellen -> key:value Paar
    params = {"name": name} #Parameter erstellen -> ein key:value Paar
    cursor.execute(query, params) #Query ausführen
    row = cursor.fetchone() #Ergebnis auslesen -> Tuple
    if row:
        return row_to_model(row) #Zeile in ein Model umwandeln
    else:
        raise MissingParameterError(message=f"Parameter with name {name} not found") #Fehler, falls der Parameter in der Datenbank nicht gefunden wurde

def get_parameters() -> list[Parameter]: #Alle Parameter aus der Datenbank auslesen
    query = "SELECT * FROM PARAMETER" #Query erstellen
    cursor.execute(query) #Query ausführen
    rows = list(cursor.fetchall()) #Alle Ergebnisse auslesen -> Liste von Tuples
    return [row_to_model(row) for row in rows] #Alle Zeilen in ein Model umwandeln -> List-Comprehension

def create_parameter(parameter: Parameter) -> Parameter: #Einen Parameter in die Datenbank einfügen
    query = "INSERT INTO PARAMETER VALUES(:id, :name, :unit, :value)" #Query erstellen
    params = model_to_dict(parameter) #Model Parameter in ein Dict mit mehreren key:value Paaren umwandeln
    try:
        cursor.execute(query, params) #Query ausführen
    except IntegrityError: #Ausnahme, falls der Parameter bereits in der Datenbank vorhanden ist
        raise DuplicateParameterError(message=f"Parameter with name {parameter.name} already exists") #Fehlermeldung -> 400 Bad Request
    connection.commit() #Änderungen speichern
    return get_parameter(parameter.name) #Parameter zurückgeben -> gemäss dem Namen

def update_parameter(name: str, parameter: Parameter) -> Parameter: #Einen Parameter in der Datenbank verändern
    query = "UPDATE PARAMETER SET name=:name, unit=:unit, value=:value WHERE name=:name_original" #Query erstellen
    params = model_to_dict(parameter) #Model Parameter in ein Dict umwandeln
    params["name_original"] = name #Original Name in das Dict hinzufügen -> key:value Paar
    cursor.execute(query, params) #Query ausführen
    if cursor.rowcount == 1: #Wenn die Zeile geändert wurde
        connection.commit() #Änderungen speichern
        return get_parameter(parameter.name) #Parameter zurückgeben -> gemäss dem Namen
    else: #Wenn die Zeile nicht geändert wurde
        raise MissingParameterError(message=f"Parameter with name {name} not found") #Fehlermeldung -> 404 Not Found

def replace_parameter(name: str, parameter: Parameter) -> Parameter: #Einen Parameter in der Datenbank ersetzen
    query = "UPDATE PARAMETER SET name=:name, unit=:unit, value=:value WHERE name=:name_original" #Query erstellen
    params = model_to_dict(parameter) #Model Parameter in ein Dict umwandeln
    params["name_original"] = name #Original Name in das Dict hinzufügen -> key:value Paar
    cursor.execute(query, params) #Query ausführen
    if cursor.rowcount == 1: #Wenn die Zeile geändert wurde
        connection.commit() #Änderungen speichern
        return get_parameter(parameter.name) #Parameter zurückgeben -> gemäss dem Namen
    else: #Wenn die Zeile nicht geändert wurde
        raise MissingParameterError(message=f"Parameter with name {name} not found") #Fehlermeldung -> 404 Not Found

def delete_parameter(name: str) -> None: #Einen Parameter in der Datenbank löschen
    query = "DELETE FROM PARAMETER WHERE name=:name" #Query erstellen -> key:value Paar
    params = {"name": name} #Parameter erstellen -> ein key:value Paar
    cursor.execute(query, params) #Query ausführen
    if cursor.rowcount != 1: #Wenn keine Zeile gelöscht wurde
        raise MissingParameterError(message=f"Parameter with name {name} not found") #Fehlermeldung -> 404 Not Found
    connection.commit() #Änderungen speichern
    return None #None zurückgeben
