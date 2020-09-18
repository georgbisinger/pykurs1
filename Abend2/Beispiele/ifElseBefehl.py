# Beispiel für den else-Befehl
# Verarbeiten einer Tastatureingabe

betrag = input("Betrag?")

betrag = int(betrag)

if betrag < 0:
    print("Der Betrag ist zu klein...")
else:
    print("Der Betrag passt...")
