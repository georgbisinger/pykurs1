# GUIs mit tkInter - Beispiel Nr. 8 - ein einfaches Eingabedialogfeld - Teil 2
# Alle Beispiele ohne Klasse, da das Thema erst am Abend 5 an die Reihe kommt

import tkinter
from tkinter import messagebox

tk = tkinter.Tk()
tk.title("tkInter - Beispiel Nr. 8")
tk.geometry("400x200")

def buttonClick():
    txt1 = ent1.get()
    txt2 = ent2.get()
    messagebox.showinfo("Titel", f"Die Eingabe: {txt1} und {txt2}")

# Wenn das Widget später nicht angesprochen wird, muss keine Variable verwendet werden
tkinter.Label(tk, text="Dein Name:").pack()
ent1 = tkinter.Entry(width=40, font=("Helvetica",16, "normal"))
ent1.pack()
tkinter.Label(tk, text="Deine E-Mail-Adresse:").pack()
ent2 = tkinter.Entry(width=40, font=("Helvetica",16, "normal"))
ent2.pack()

btn1 = tkinter.Button(tk, text="OK", bg="lightblue",command=buttonClick, width=12)
btn1.pack()

tk.mainloop()