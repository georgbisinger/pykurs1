# Beispiel für den elif-Befehl
# Verarbeiten einer Tastatureingabe

betrag = input("Betrag?")

betrag = int(betrag)

if betrag < 0:
    print("Der Betrag ist zu klein...")
elif betrag > 1000:
    print("Der Betrag ist zu groß...")
else:
    print("Der Betrag passt...")
