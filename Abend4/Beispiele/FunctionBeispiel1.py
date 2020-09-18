# Ein Beispiel für eine Function (ohne Parameter)

def Kennwort():
    import random
    Kennwort = ""
    for i in range(8):
        Kennwort += chr(random.randint(33,97))
    return Kennwort


print(Kennwort())

k1 = Kennwort()
k2 = k1 + Kennwort()

print(k2)