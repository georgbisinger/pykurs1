# Ein Beispiel für eine Function mit Parameter

def Kennwort(Anzahl):
    import random
    Kennwort = ""
    for i in range(Anzahl):
        Kennwort += chr(random.randint(33,97))
    return Kennwort


print(Kennwort(4))

print(Kennwort(24))

print(Kennwort())
