# Die Eingabe in eine Textdatei schreiben

txtDateipfad = "Eingabe.txt"

anzahl = 0
with open(txtDateipfad, "w") as fh:
    while True:
        Eingabe = input("Gib einen Namen ein (Abbruch mit 'Q') ")
        if Eingabe == "Q":
            break
        fh.write(Eingabe + '\n')
        anzahl += 1

print("Es wurden %d Namen gespeichert" % anzahl)

# Wo wurde die Datei gespeichert?