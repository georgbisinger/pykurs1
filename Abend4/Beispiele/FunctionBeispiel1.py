# Ein Beispiel für eine Function (ohne Parameter)

def Kennwort():
    import random
    wort = ""
    for i in range(8):
        wort += chr(random.randint(33,97))
    return wort


print(Kennwort())

k1 = Kennwort()
k2 = k1 + Kennwort()

print(k2)