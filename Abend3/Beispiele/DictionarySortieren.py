# Ein Dictionary mit Städtenamen und Einwohnerzahlen sortieren

staedte = {"Göppingen":("GP", 57558), "Nürtingen":("NT", 41097), "Kirchheim Teck":("ES", 40585), 
           "Esslingen":("ES", 93304), "Plochingen":("ES", 14139), "Böblingen":("BB", 50155), "Stuttgart":("S", 634830)}

print("Die Liste enthält %d Städte" % len(staedte))

# Nach was soll sortiert werden?

# Am einfachsten wird nach den Schlüsseln sortiert, also nach den Städtenamen

staedteSortiert = sorted(staedte)

# In dieser Schreibweise werden die Schlüssel durchlaufen
for stadt in staedteSortiert:
    print("%s hat %d Einwowhner" % (stadt, staedte[stadt][1]))

# Soll nach einem Wert sortiert werden, wird es leider etwas komplizierter
# Wie wird dem Sortierer gesagt, nach welchem Wert "er" sortieren soll?
# Hier ist ein sog. Lambda die "einfachste Lösung"

# Es soll nach dem Kfz-Kennzeichen sortiert werden

kfzSortiert = sorted(staedte.values(), key=lambda t: t[0])
print("Ausgabe sortiert nach dem Kfz-Kennzeichen mit Kfz-Kennzeichen")
for kfz, einwohner in kfzSortiert:
    print("%s hat %d Einwohner" % (kfz, einwohner))

# Es soll aber der Name der Stadt ausgegeben werden, also der Key ???

kfzSortiert = sorted(staedte.items(), key=lambda t: t[0])
# Die Rückgabe ist eine Liste mit ('Kfz',(Stadt, Einwohnerzahl))-Tupels
print("Ausgabe sortiert nach dem Kfz-Kennzeichen mit dem Namen der Stadt")
for stadt in kfzSortiert:
    print("%s hat %d Einwohner" % (stadt[0], stadt[1][1]))

# Jetzt soll auch das Kfz-Kennzeichen mit ausgegeben werden
