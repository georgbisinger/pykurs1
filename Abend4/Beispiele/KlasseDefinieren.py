# Definieren einer Klasse für eine Hotelreservierung

class Reservierung:
    # Diese Angaben sind optional
    Anreise = ""
    Abreise = ""
    Gastname = ""
    ZimerTyp = ""
    Anzahl = 0

# Anlegen eines Objekts
r1 = Reservierung
# Zuweisen an die Attribute
r1.Abreise = "23.7.2020"
r1.Abreise = "30.7.2020"
r1.Gastname = "Gerhard Schröder"
r1.ZimerTyp = "1 D7"
r1.Anzahl = 1

# Es können jederzeit neue Attribute festgelegt werden
r1.Extras = "Zwei Kissen"

# Ausgabe aller Attribute
print(dir(r1))

# Wichtig: Diese Form der Definition ist nicht wirklich praxistauglich - es fehlt der Konstruktor
