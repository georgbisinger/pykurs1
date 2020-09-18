# Ein Dictionary mit Städtenamen und Einwohnerzahlen

staedte = {"Göppingen":57558, "Nürtingen":41097, "Kirchheim Teck":40585, 
           "Esslingen":93304, "Plochingen":14139, "Böblingen":50155, "Stuttgart":634830}

print("Die Liste enthält %d Städte" % len(staedte))

# Die Einwohnerzahl von Esslingen
print(staedte["Esslingen"])

# Die Einwohnerzahl von Kirchheim
print(staedte["Kirchheim Teck"])

# In dieser Schreibweise werden die Schlüssel durchlaufen
for stadt in staedte:
    print("%s hat %d Einwowhner" % (stadt, staedte[stadt]))
