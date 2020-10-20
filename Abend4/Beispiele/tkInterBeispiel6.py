# GUIs mit tkInter - Beispiel Nr. 6 - Anzeige einer Messagebox
# Alle Beispiele ohne Klasse, da das Thema erst am Abend 5 an die Reihe kommt

import tkinter
from tkinter import messagebox

tk = tkinter.Tk()
tk.title("tkInter - Beispiel Nr. 6")
tk.geometry("320x160")

def buttonClick():
    messagebox.showinfo("Titel", "Vielen Dank für das Anklicken")

btn1 = tkinter.Button(tk, text="Button 1", bg="lightblue",command=buttonClick)
# side legt den Rand fest, an dem das Widget platziert wird
btn1.pack(side=tkinter.LEFT)

btn2 = tkinter.Button(tk, text="Button 2", bg="lightyellow",command=buttonClick)
# padx legt den Abstand nach links und rechts fest
btn2.pack(side=tkinter.LEFT)

btn3 = tkinter.Button(tk, text="Button 3", bg="lightgreen",command=buttonClick)
btn3.pack(side=tkinter.LEFT)

tk.mainloop()