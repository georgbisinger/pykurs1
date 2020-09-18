# Abfrage des heutigen Datums
import datetime

heute = datetime.datetime.today()

# Ausgabe des Datums ohne Formatierung
print(heute)

# Jetzt soll nur das Datum ausgegeben werden
# Dazu muss man die Formatbezeichner kennen, z.B. %d für den Tag, %m für den Monat und natürlich %Y für das Jahr
# Es kommt auf die Groß-/Kleinschreibung an!

# Die Datumsformat-Function heißt strftime() - nicht zu verwechseln mit strptime(), die aus einer Zeichenkette ein DateTime-Objekt macht

print(heute.strftime("%d.%m.%Y"))

# Die Bestandteile eines DateTime-Objekts lassen sich auch einzeln ansprechen

print("Das aktuelle Jahr: %d" % heute.year)

print("Der aktuelle Monat: %d" % heute.month)

print("Der aktuelle Tag: %d" % heute.day)