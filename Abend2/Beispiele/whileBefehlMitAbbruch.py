# Beispiel für den while-Befehl mit Abbruchbedingung
import time

i = 0
while i < 10:
    i += 1
    time.sleep(1)
    print("Durchlauf Nr. %d" % i)