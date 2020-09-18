# Beispiel für den for-Befehl
# Schaltjahre ausgeben im Rahmen einer Wiederholung

# Nur ein willkürlicher Bereich - wichtig: Die range()-Function "läuft" nur bis zum Endwert -1
for jahr in range(1900, 2200):
    if jahr % 400 == 0:
        schaltjahr = True
    elif jahr % 100 == 0:
        schaltjahr = False
    elif jahr % 4 == 0:
        schaltjahr = True
    else:
        schaltjahr = False

    if schaltjahr == True:
         # print("Das Jahr " + str(jahr) + " ist ein Schaltjahr")
         print(f"Das Jahr {jahr} ist keine Schaltjahr")
    #else:
        # print("Das Jahr " + str(jahr) + " ist kein Schaltjahr")
               