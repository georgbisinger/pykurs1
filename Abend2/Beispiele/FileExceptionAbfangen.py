# Beispiel für den try- und except-Befehl
# Einlesen einer Textdatei

dateiPfad = "Material/Gewichtsdaten.txt"

try:
    with open(dateiPfad, 'r', encoding='utf-8') as fh:
        for zeile in fh:
            print(zeile)
# except:
#    print("!!! Fehler - Die Datei kann nicht geöffnet werden!!!")
except Exception as e:
    print(f"!!! Fehler - Die Datei kann nicht geöffnet werden!!! - Fehler: {str(e)}")
