# GUIs mit tkInter - Beispiel Nr. 5 - Mehrere Buttons nebeneinander
# Alle Beispiele ohne Klasse, da das Thema erst am Abend 5 an die Reihe kommt

import tkinter

tk = tkinter.Tk()
tk.title("tkInter - Beispiel Nr. 5")
tk.geometry("600x400")

btn1 = tkinter.Button(tk, text="Button 1", bg="lightblue",width=24, height=2)
# side legt den Rand fest, an dem das Widget platziert wird
btn1.pack(side=tkinter.LEFT)

btn2 = tkinter.Button(tk, text="Button 2", bg="lightyellow",width=24, height=2)
# padx legt den Abstand nach links und rechts fest
btn2.pack(side=tkinter.LEFT,padx=(20,20))

btn3 = tkinter.Button(tk, text="Button 3", bg="lightgreen",width=24, height=2)
btn3.pack(side=tkinter.RIGHT)

tk.mainloop()