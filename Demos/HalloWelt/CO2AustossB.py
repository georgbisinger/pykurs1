# Wie hoch ist der CO2-Ausstoß meines Autos?

# Diese Variante fragt auch die gefahrenen km ab

# Wichtig: Wir brauchen einen Wert vom Typ float!
verbrauch = (float)(input("Verbrauch in l/100km (z.B. 5.5) "))
# Dieses Mal soll ein Integer-Wert entstehen
km = (int)(input("Gefahrene km?"))

# Bei dieser Eingabe ist der Typ einfach str (String)
kraftstoffArt = input("Diesel oder Benziner (D oder B)?")

if kraftstoffArt[0].upper() == "D":
    co2 = verbrauch * 26.5 / 100 * km
else:
    co2 = verbrauch * 23.7 / 100 * km

# Die formatierte Ausgabe von Zahlen und Datumsangaben wirkt am Anfang leider etwas "speziell"
print("Der CO2-Ausstoß beträgt für %d gefahrene Km: %.2f g CO2/km" % (km, co2))

