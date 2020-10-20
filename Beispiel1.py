# Energiekostenrechner

verbrauch = input("Verbrauch in Watt?")

dauer = input("Dauer in Minuten?")

kostenKw = 0.3

kosten = int(verbrauch) / 1000 * kostenKw * int(dauer) / 60

print("Die Kosten sind: %d" % kosten)

