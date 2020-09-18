# Beispiel für eine Zahleneingabe

eingabeOK = False

while not eingabeOK:
    eingabe = input("Zahl?")
    try:
        zahl = float(eingabe)
        eingabeOK = True
    except:
        print("Eingabe bitte wiederholen")

print("Eingabe war OK, vielen Dank!")
