# Enthält nur die Function-Definition

def Kennwort(Anzahl=8):
    import random
    Kennwort = ""
    for i in range(Anzahl):
        Kennwort += chr(random.randint(33,97))
    return Kennwort


# Kein automatischer Aufruf, wenn die Datei über import ausgeführt wird

if __name__ == "__main__":
    print(Kennwort())