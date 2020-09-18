# Ein Beispiel für eine Function mit einer variablen Anzahl an Parametern

def Kennwort(**args):
    import random
    Kennwort = ""
    if not args.get("Anzahl") == None:
        Anzahl = args["Anzahl"]
    else:
        Anzahl = 8
    if not args.get("NurAlpha") == None:
        Min = 48
        Max = 90
    else:
        Min = 33
        Max = 96
    for i in range(Anzahl):
        Kennwort += chr(random.randint(Min, Max))
    return Kennwort

print(Kennwort())

print(Kennwort(Anzahl=4))

print(Kennwort(**{"Anzahl":4,"NurAlpha":True}))
