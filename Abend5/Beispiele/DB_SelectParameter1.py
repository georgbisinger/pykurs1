# Select-Abfrage mit einem Parameter mit einer SQLite-Datenbank

from os import path
import sqlite3
from sqlite3 import Error

# Nur bei VSCode erforderlich bzw. wenn sich die py-Datei nicht im aktuellen Verzeichnis befindet

curPfad = path.dirname(__file__)
dbPfad = path.join(curPfad, r"Material\\PyMusik.db")

conDb = None

try:
    # Schritt 1: Verbindung herstellen
    # Wichtig: Es gibt keine Fehlermeldung, wenn die Db-Datei nicht existiert - sie wird immer neu angelegt!
    conDb = sqlite3.connect(dbPfad)
    # Schritt 2: Anlegen eines Cursors
    cursorDb = conDb.cursor()
    # Schritt 3: Ausfuehren eines SQL-Kommandos
    Jahr = 1985
    cursorDb.execute("Select * From Titel Where Jahr=?", [Jahr])
    # Erfolgsmeldung ausgeben
    print("*** Die Select-Abfrage wurde ausgefuehrt ***")
    # Schritt 4: Hole alle Datensaetze als Liste
    alleTitel = cursorDb.fetchall()
    for titel in alleTitel:
        print(titel)
except Error as e:
    print(f"!!! Fehler beim Herstellen der Verbindung ({e})")
finally:
    if not conDb is None:
        conDb.close()
        print("*** Die Verbindung wurde wieder geschlossen ***")
