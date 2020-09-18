# Ein Beispiel für eine Function
import random

def Lottozahlen(anzahl):
    zahlen = []
    for i in range(0, anzahl+1):
        zahlen.append(random.randint(1,49))
    return zahlen

print(Lottozahlen(6))
