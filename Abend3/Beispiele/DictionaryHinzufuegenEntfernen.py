# Hinzufügen und Entfernen von Einträgen zu einem Dictionary

staedte = {"Göppingen":57558, "Nürtingen":41097, "Kirchheim Teck":40585, 
           "Esslingen":93304, "Plochingen":14139, "Böblingen":50155, "Stuttgart":634830}

print("Die Liste enthält %d Städte" % len(staedte))

staedte["Waiblingen"] = 55449

print("Die Liste enthält %d Städte" % len(staedte))

# Variante A
staedte.pop("Esslingen")

print("Die Liste enthält %d Städte" % len(staedte))

# Variante B
del staedte["Plochingen"]

print("Die Liste enthält %d Städte" % len(staedte))

# Entfernen mit Fehlervermeidung
try:
    del staedte["Plochingen"]
except:
    print("Schlüssel nicht vorhanden")

print("Die Liste enthält %d Städte" % len(staedte))
