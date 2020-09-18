# Es gibt viele Gründe für einen Ausführungsfehler (exception)
import math

zahl = input("Gib eine Zahl ein ")

# Jetzt soll die Quadratwurzel gezogen werden
# Welche Sorte von Ausführungsfehler (Exception) tritt hier auf?
wurzel = math.sqrt(zahl)

# Dieser Befehl wird nicht mehr ausgeführt, da die Programmausführung vorher abbricht
print("Das Ergebnis ist %.2f" % wurzel)