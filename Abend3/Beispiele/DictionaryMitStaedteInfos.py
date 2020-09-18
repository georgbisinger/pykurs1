# Ein Dictionary mit meheren Infos zu einer Stadt

staedte = {"Göppingen":("GP", 57558), "Nürtingen":("NT", 41097), "Kirchheim Teck":("ES", 40585), 
           "Esslingen":("ES", 93304), "Plochingen":("ES", 14139), "Böblingen":("BB", 50155), "Stuttgart":("S", 634830)}

print("Die Liste enthält %d Städte" % len(staedte))

# Die Einwohnerzahl von Esslingen
print(staedte["Esslingen"][1])

# Das Kfz-Kennzeichen von Böblingen
print(staedte["Böblingen"][0])

# In dieser Schreibweise werden die Schlüssel durchlaufen
for stadt in staedte:
    print("%s hat %s als Kfz-Kennzeichen und %d Einwowhner" % (stadt, staedte[stadt][0],staedte[stadt][1]))
