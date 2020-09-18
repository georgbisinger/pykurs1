# Suchen in einer Liste

staedte = ["Göppingen", "Nürtingen", "Kirchheim Teck", "Esslingen", "Plochingen", "Böblingen", "Stuttgart"]

stadt = input("Name einer Stadt?")

# Prüfen, ob ein Element in einer Liste enthalten ist oder nicht
if stadt in staedte:
    print("%s ist in der Liste enthalten" % stadt)
else:
    print("%s ist nicht in der Liste enthalten" % stadt)


# Die Position eines Elements in einer Liste ausgeben
index = staedte.index(stadt)
print("%s ist an Positon %d zu finden" % (stadt, index + 1))

# ist die Stadt nicht in der Liste enthalten, gibt es eine Fehlermeldung - wie kann die Meldung verhindert werden?