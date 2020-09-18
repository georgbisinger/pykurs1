# Eingaben über die input-Function

# Ich kann "alles" eingeben, da die Rückgabe ein str ist
alter = input("Wie alt bis Du?")

# %s steht für ein str
print("Du bist %s Jahre alt" % alter)

# Ich muss eine Zahl eingeben, da die eingabe per int() in eine Zahl konvertiert wird
alter = int(input("Wie alt bis Du?"))

# %d steht für einen int
print("Du bist %d Jahre alt" % alter)

