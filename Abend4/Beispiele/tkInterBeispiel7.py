# GUIs mit tkInter - Beispiel Nr. 7 - ein einfaches Eingabedialogfeld - Teil 1
# Alle Beispiele ohne Klasse, da das Thema erst am Abend 5 an die Reihe kommt

import tkinter
from tkinter import messagebox

tk = tkinter.Tk()
tk.title("tkInter - Beispiel Nr. 7")
tk.geometry("320x160")

def buttonClick():
    messagebox.showinfo("Titel", "Vielen Dank für das Anklicken")

lbl1 = tkinter.Label(tk, text="Dein Name:")
lbl1.pack()
btn1 = tkinter.Button(tk, text="OK", bg="lightblue",command=buttonClick, width=12)
btn1.pack()

tk.mainloop()