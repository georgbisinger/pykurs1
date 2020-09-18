# Beispiel für den if- und else-Operator

for z in range(1,100):
    print("Die Zahl ist gerade" if z % 2 == 0 else "Die Zahl ist ungerade")
    # print("Die Zahl ist " + ("gerade" if z % 2 == 0 else "ungerade"))
    # print("%d ist gerade" % z if z % 2 == 0 else "%d ist ungerade" % z)