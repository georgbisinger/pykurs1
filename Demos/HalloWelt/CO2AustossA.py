# Wie hoch ist der CO2-Ausstoß meines Autos?

# Quelle der Formel: Deutsche Handwerks Zeitung

# Benzin: Verbrauch pro 100 Kilometer mit 23,8 multiplizieren.
# Beispiel: 8 Liter/100 km = 8 mal 23,8 = 190,4 g CO2/km
# Diesel: Verbrauch pro 100 Kilometer mit 26,5 multiplizieren.
# Beispiel: 5,5 Liter/100 km = 5,5 mal 26,5 = 145,8 g CO2/km

# Wichtig: Wir brauchen einen Wert vom Typ float!
# Ein String ist für die spätere formatierte Ausgabe nicht geeignet

verbrauch = (float)(input("Verbrauch in l/100km (z.B. 5.5) "))

kraftstoffArt = input("Diesel oder Benziner (D oder B)?")

if kraftstoffArt[0].upper() == "D":
    co2 = verbrauch * 26.5
else:
    co2 = verbrauch * 23.7

print("Der CO2-Ausstoß beträgt: %.2f g CO2/km" % co2)

