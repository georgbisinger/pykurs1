# GUIs mit tkInter - Beispiel Nr. 3 - Anzeigen eines anklickbaren Buttons
# Alle Beispiele ohne Klasse, da das Thema erst am Abend 5 an die Reihe kommt

import tkinter

tk = tkinter.Tk()
tk.title("tkInter - Beispiel Nr. 3")
tk.geometry("800x600")

btn1 = tkinter.Button(tk, text="Button 1", bg="lightblue",width=24, height=2)
btn1.pack()

tk.mainloop()