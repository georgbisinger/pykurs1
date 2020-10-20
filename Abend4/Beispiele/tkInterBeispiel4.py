# GUIs mit tkInter - Beispiel Nr. 4 - mehrere Buttons untereinander
# Alle Beispiele ohne Klasse, da das Thema erst am Abend 5 an die Reihe kommt

import tkinter

tk = tkinter.Tk()
tk.title("tkInter - Beispiel Nr. 4")
tk.geometry("400x200")

btn1 = tkinter.Button(tk, text="Button 1", bg="lightblue",width=24, height=2)
btn1.pack()

btn2 = tkinter.Button(tk, text="Button 2", bg="lightyellow",width=24, height=2)
btn2.pack()

btn3 = tkinter.Button(tk, text="Button 3", bg="lightgreen",width=24, height=2)
btn3.pack()

tk.mainloop()