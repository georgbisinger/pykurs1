# Beispiel für den break-Befehl
import random

# Es sollen nur ungerade Zahlen ausgegeben werden
while True:
    z = random.randint(1,100)
    if z % 2 == 0:
        break
    print(z)