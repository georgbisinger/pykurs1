# Herstellen einer Verbindung zu einer SQLite-Datenbank

from os import path
import sqlite3
from sqlite3 import Error

# Nur bei VSCode erforderlich bzw. wenn sich die py-Datei nicht im aktuellen Verzeichnis befindet

curPfad = path.dirname(__file__)
dbPfad = path.join(curPfad, r"Material\\PyMusik.db")

conDb = None

try:
    # Verbindung herstellen
    # Wichtig: Es gibt keine Fehlermeldung, wenn die Db-Datei nicht existiert - sie wird immer neu angelegt!
    conDb = sqlite3.connect(dbPfad)
    # Ausführen einer Datenbankabfrage, um zu testen, ob die Db-Datei angesprochen werden kann
    conDb.execute("Select * From Titel")
    # Erfolgsmeldung ausgeben
    print("*** Die Verbindung wurde hergestellt ***")
except Error as e:
    print(f"!!! Fehler beim Herstellen der Verbindung ({e})")
finally:
    if not conDb is None:
        conDb.close()
        print("*** Die Verbindung wurde wieder geschlossen ***")
