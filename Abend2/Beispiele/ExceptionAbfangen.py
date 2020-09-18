# Ein Ausführungsfehler wird abgefangen
import math

zahl = input("Gib eine Zahl ein ")

# Jetzt soll die Quadratwurzel gezogen werden
# Welche Sorte von Ausführungsfehler (Exception) tritt hier auf?
try:
    wurzel = math.sqrt(zahl)
except:
    print("!!! Fehler bei der Berechnung !!!")
    wurzel = 0

# Dieser Befehl wird nicht mehr ausgeführt, da die Programmausführung vorher abbricht
print("Das Ergebnis ist %.2f" % wurzel)