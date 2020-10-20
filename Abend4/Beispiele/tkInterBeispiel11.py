# GUIs mit tkInter - Beispiel Nr. 11 - ein einfaches Eingabedialogfeld - Teil 6
# Alle Beispiele ohne Klasse, da das Thema erst am Abend 5 an die Reihe kommt

import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("tkInter - Beispiel Nr. 11")
win.geometry("600x200")

def buttonClick():
    txt1 = ent1.get()
    txt2 = ent2.get()
    messagebox.showinfo("Titel", f"Die Eingabe: {txt1} und {txt2}")

email_text = tk.StringVar()
name_text = tk.StringVar()

tk.Label(win, text="Dein Name:").grid(row=1, column=1)
ent1 = tk.Entry(width=36, font=("Helvetica",16, "normal"),textvariable=name_text)
ent1.grid(row=1, column=2)

tk.Label(win, text="Deine E-Mail-Adresse:").grid(row=2, column=1)
ent2 = tk.Entry(width=36, font=("Helvetica",16, "normal"),textvariable=email_text)
# pady sorgt für etwas vertikalen Abstand
ent2.grid(row=2, column=2, pady=20)

name_text.set("<Hier Name>")
email_text.set("<Hier EMail-Adresse>")

btn1 = tk.Button(win, text="OK", bg="lightblue",command=buttonClick, width=16, height=2)
btn1.grid(row=3, column=1, columnspan=2)

win.mainloop()