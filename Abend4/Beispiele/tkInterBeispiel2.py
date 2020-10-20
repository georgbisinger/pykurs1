# GUIs mit tkInter - Beispiel Nr. 2 - Anzeigen eines leeren Fensters mit fester Größe und Titelzeile
# Alle Beispiele ohne Klasse, da das Thema erst am Abend 5 an die Reihe kommt

import tkinter

tk = tkinter.Tk()
tk.title("tkInter - Beispiel Nr. 2")
tk.geometry("800x600")
# Sorgt dafür, dass sich die Größe des Fensters nicht ändern lässt
# tk.resizable(0, 0)
tk.mainloop()