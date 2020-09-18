# Ein Konstruktor mir einer variablen Zahl an Parametern
from datetime import date

class Reservierung:

    # Definition des Konstruktors
    def __init__(self, **kwargs):
        self.DatumReservierung = date.today().strftime("%d.%m.%y")
        if kwargs.get("Anreise") != None:
            self.Anreise = kwargs["Anreise"]
        if kwargs.get("Abreise") != None:
            self.Abreise = kwargs["Abreise"]
        if kwargs.get("Gastname") != None:
            self.Gast = kwargs["Gastname"]
        if kwargs.get("ZimmerTyp") != None:
            self.ZimmerTyp = kwargs["ZimmerTyp"]
        else:
            self.ZimmerTyp = "EZ"
        if kwargs.get("AnzahlZimmer") != None:
            self.AnzahlZimmer = kwargs["AnzahlZimmer"]
        else:
            self.AnzahlZimmer = 0

    # Definition eines weiteren Attributs als Function
    def __toString__(self):
        return f"Gast={self.Gast} - Anreise={self.Anreise} - Abreise: {self.Abreise} - Zimmertyp: {self.ZimmerTyp} - Anzahl Zimmer: {self.AnzahlZimmer}"

Anreise = "23.7.2020"
Abreise = "30.7.2020"
Gast = "Edwald Ziegler"
ZimmerTyp = "DZ"
Anzahl = 1

# Konstruktor mit allen Parametern
r1 = Reservierung(Anreise=Anreise, Abreise=Abreise, Gastname=Gast, ZimmerTyp=ZimmerTyp, AnzahlZimmer=Anzahl)
print(r1.__toString__())

# Konstruktor mit wenigen Parametern
Anreise = "31.7.2020"
Abreise = "2.8.2020"
Gast = "Alfons Dinkelbeck"
r2 = Reservierung(Anreise=Anreise, Abreise=Abreise, Gastname=Gast)

print(r2.__toString__())

# In der Praxis kommen die Daten für die Objekte z.B. aus einer Datei, Datenbank oder Webservice-Aufruf