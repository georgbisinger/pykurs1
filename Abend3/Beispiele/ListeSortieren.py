# Sortieren einer Liste mit der sorted()-Function und dem sort()-Attribut

staedte = ["Göppingen", "Nürtingen", "Kirchheim Teck", "Esslingen", "Plochingen", "Böblingen", "Stuttgart"]

print("Die Liste enthält %d Städte" % len(staedte))

# Sortierung mit neuer Liste als Ergebnis
staedteSortiert = sorted(staedte)

for stadt in staedteSortiert:
    print("Die attraktivste Stadt in der Region ist: %s" % stadt)

print()

# Inplace-Sortierung
staedte.sort(reverse=True) # reverse ist ein optionaler Parameter, der die Sortierreihenfolge umdreht
for stadt in staedte:
    print("Die attraktivste Stadt in der Region ist: %s" % stadt)

