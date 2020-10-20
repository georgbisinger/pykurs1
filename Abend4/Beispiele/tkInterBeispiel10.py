# GUIs mit tkInter - Beispiel Nr. 10 - ein einfaches Eingabedialogfeld - Teil 4
# Alle Beispiele ohne Klasse, da das Thema erst am Abend 5 an die Reihe kommt

import tkinter
from tkinter import messagebox

tk = tkinter.Tk()
tk.title("tkInter - Beispiel Nr. 10")
tk.geometry("400x200")

def buttonClick():
    txt1 = ent1.get()
    messagebox.showinfo("Titel", f"Das Kennwort: {txt1}")

# Variante 1 für das Setzen von Text
tkinter.Label(tk, text="Kennwort:").pack()
ent1 = tkinter.Entry(show="*")
ent1.pack()

btn1 = tkinter.Button(tk, text="OK", bg="lightblue",command=buttonClick, width=12)
btn1.pack()

tk.mainloop()