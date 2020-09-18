# Eine py-Datei mit mehreren Functions

def Kennwort(Anzahl):
    import random
    Kennwort = ""
    for i in range(Anzahl):
        Kennwort += chr(random.randint(33,97))
    return Kennwort

def Zufallszahl(Min=1, Max=10):
    import random
    return random.randint(Min, Max)