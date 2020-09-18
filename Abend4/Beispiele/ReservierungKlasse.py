# Definition der Klasse Reservierung
from datetime import date

class Reservierung:

    # Definition des Konstruktors
    def __init__(self, Nr, Anreise, Abreise, Gastname, ZimmerTyp, Anzahl):
        self.DatumReservierung = date.today().strftime("%d.%m.%y")
        self.Nr = Nr
        self.Anreise = Anreise
        self.Abreise = Abreise
        self.Gast = Gastname
        self.Typ = ZimmerTyp
        self.Anzahl = Anzahl
        self.AnzahlUeb = 1     # Hier müsste die Anzahl an Übernachtungen eingetragen werden -  die 1 ist daher nur provisorisch
        
    # Definition eines weiteren Attributs als Function
    def __toString__(self):
        return f"Datum: {self.DatumReservierung} - Nr={self.Nr} - Gast={self.Gast} - Anreise={self.Anreise} - Abreise: {self.Abreise} - Anzahl Zimmer: {self.Anzahl}"
