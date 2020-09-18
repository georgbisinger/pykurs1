# Beispiel für den continue-Befehl
import datetime

# Alle Tage des Monats durchgehen
# weekday() liefert die Nummer des Wochentags, 6 = Sonntag

# Aktuelle Monat
heute = datetime.datetime.today()
monat = heute.month
jahr = heute.year
# Wichtig: Die 31 stimmt nicht immer - wie bekommt die Anzahl an Tagen pro Monat heraus?
for t in range(1, 31):
    tag = datetime.datetime(jahr, monat, t)
    if tag.weekday() == 5 or tag.weekday() == 6:
        continue
    print("Der %ste ist ein Wochentag" % tag.day)
