import os
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

connection: Connection | None = None #Verbindung zur Datenbank
cursor: Cursor | None = None #Cursor für die Datenbank

def init(name: str | None = None, reset: bool = False): #Init der Datenbank
    global connection, cursor #Globale Variablen
    if connection and not reset:
        return
    connection = None
    
    if not name: #Wenn kein Name vorhanden ist -> Name aus der Environment Variable DATABASE_NAME auslesen
        name = os.getenv("DATABASE_NAME")
        top_dir = Path(__file__).resolve().parents[1] #Top Directory auslesen
        db_dir = top_dir / "db" #DB Directory auslesen
        db_name = "database.db" #DB Name auslesen
        db_dir.mkdir(parents=True, exist_ok=True) #DB Directory erstellen, falls nicht vorhanden
        db_path = str(db_dir / db_name) #DB Path auslesen
        name = os.getenv("DATABASE_NAME", db_path) #Wenn kein Name vorhanden ist -> DB Path auslesen
    
    Path(name).parent.mkdir(parents=True, exist_ok=True) #Übergeordneten Ordner anlegen, falls nötig
    connection = connect(name, check_same_thread=False) #Verbindung zur Datenbank herstellen    
    cursor = connection.cursor() #Cursor für die Datenbank erstellen

init() #Funktion ausführen
