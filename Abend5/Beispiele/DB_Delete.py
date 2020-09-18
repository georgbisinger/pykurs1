# Delete - Löschen von Datensätzen aus einer SQLite-Datenbank

from os import path
import sqlite3
from sqlite3 import Error

# Nur bei VSCode erforderlich bzw. wenn sich die py-Datei nicht im aktuellen Verzeichnis befindet

curPfad = path.dirname(__file__)
dbPfad = path.join(curPfad, r"Material\\PyMusik.db")

conDb = None

try:
    # Schritt 1: Verbindung herstellen
    conDb = sqlite3.connect(dbPfad)
    # Schritt 2: Ausfuehren eines SQL-Kommandos
    # sqlCmd = "Delete From Titel Where Kategorie ='PopX'"
    sqlCmd = "Delete From Titel Where Id=26"
    conDb.execute(sqlCmd)
    # Schritt 3: Änderung bestätigen
    conDb.commit()
    print("*** Der/die Datensätze wurden gelöscht ***")
    # Schritt 4: Zur Kontrolle aller Datensätze abrufen
    cursorDb = conDb.cursor()
    cursorDb.execute("Select * From Titel")
    alleTitel = cursorDb.fetchall()
    for titel in alleTitel:
        print(titel)
except Error as e:
    print(f"!!! Fehler beim Herstellen der Verbindung ({e})")
finally:
    if not conDb is None:
        conDb.close()
        print("*** Die Verbindung wurde wieder geschlossen ***")
