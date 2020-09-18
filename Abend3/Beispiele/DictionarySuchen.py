# Suchen in einem Dictionary

staedte = {"Göppingen":("GP", 57558), "Nürtingen":("NT", 41097), "Kirchheim Teck":("ES", 40585), 
           "Esslingen":("ES", 93304), "Plochingen":("ES", 14139), "Böblingen":("BB", 50155), "Stuttgart":("S", 634830)}

print("Die Liste enthält %d Städte" % len(staedte))

stadt = input("Name der Stadt? ")

if stadt in staedte:
    print("%s hat %d Einwohner" % (stadt, staedte[stadt][1]))
else:
    print("%s ist nicht in der Liste enthalten" % stadt)