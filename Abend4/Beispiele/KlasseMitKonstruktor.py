# Definieren einer Klasse für eine Hotelreservierung

class Reservierung:

    # Definition des Konstruktors
    def __init__(self, Anreise, Abreise, Gastname, ZimmerTyp, Anzahl):
        self.Anreise = Anreise
        self.Abreise = Abreise
        self.Gast = Gastname
        self.ZimmerTyp = ZimmerTyp
        self.AnzahlZimmer = Anzahl

    # Definition eines weiteren Attributs als Function
    def __toString__(self):
        return f"Gast={self.Gast} - Anreise={self.Anreise} - Abreise: {self.Abreise} - Anzahl Zimmer: {self.AnzahlZimmer}"

Anreise = "23.7.2020"
Abreise = "30.7.2020"
Gast = "Edwald Ziegler"
ZimmerTyp = "DZ"
Anzahl = 1

# Es wird ein Objekt definiert
r1 = Reservierung(Anreise, Abreise, Gast, ZimmerTyp, Anzahl)

# Ausgabe des Typs - __main__.Reservierung - __main__ ist der Name des Moduls
print(type(r1))

print(r1.__toString__())

# In der Praxis kommen die Daten für die Objekte z.B. aus einer Datei, Datenbank oder Webservice-Aufruf