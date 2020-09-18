# Ein Beispiel für die Vererbung bei Klassen

# Definition der Super-Klasse (Basisklasse)
class Person():

    def __init__(self, GebDatum, Name):
        self.GebDatum = GebDatum
        self.Name = Name

    def __toString__(self):
        return f"Name: {self.Name} GebDatum: {self.GebDatum}"

# Definition einer abgeleiteten Klasse
class Mitarbeiter(Person):

    def __init__(self, GebDatum, Name, MitarbeiterNr):
        super().__init__(GebDatum, Name)
        self.MitarbeiterNr = MitarbeiterNr

# Definition einer abgeleiteten Klasse
class Gast(Person):

    def __init__(self, GebDatum, Name, ReservierungsNr):
        super().__init__(GebDatum, Name)
        self.ReservierungsNr = ReservierungsNr


g1 = Gast("1.9.1988", "Herbert H", 1001)

print(g1.__toString__())


