# Insert-Kommando mit Parametern mit einer SQLite-Datenbank

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
    # Schritt 2: Zusammenstellen des SQL-Kommandos Insert Into
    sqlCmd = "Insert Into Titel Values(?,?,?,?,?,?,?)"
    # Schritt 3: Ausfuehren des Insert-Kommandos
    conDb.execute(sqlCmd, (26, 'Westend boys','Petshop Boys',1985,'Pop',4,3.55))
    # Schritt 4: Select-Abfrage ausfuehren
    cursorDb = conDb.execute("Select * From Titel")
    # Schritt 5: Änderung bestätigen
    conDb.commit()
    # Schritt 6: Hole alle Datensaetze als Liste
    alleTitel = cursorDb.fetchall()
    for titel in alleTitel:
        print(titel)

    # Schritt 7: Neuen Datensatz wieder loeschen
    # conDb.execute("Delete From Titel Where Id=26")
    # conDb.commit()

except Error as e:
    print(f"!!! Fehler beim Herstellen der Verbindung ({e})")
finally:
    if not conDb is None:
        conDb.close()
        print("*** Die Verbindung wurde wieder geschlossen ***")
