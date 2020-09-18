# Einfache mathematische Berechnungen mit dem math-Modul
import math

# Wir berechen 2 hoch 8 = 256 - die Rückgabe ist ein float
print(math.pow(2, 8))

# Wir berechen 2 hoch 8 = 256 - die Rückgabe ist ein int
print(int(math.pow(2, 8)))

# Wir berechnen die Quadratwurzel aus 3
print(math.sqrt(3))

# Wir berechnen den sinus von 90
print(math.sin(90))

# Wir berechnen die Fakultät 6! = 720
print(math.factorial(6))

# 3.56 abrunden
z = 3.56
print(math.floor(z))

# 3.56 aufrunden
print(math.ceil(z))

# 10er-Logarithmus von 1000
z = 1000
print(math.log10(z))