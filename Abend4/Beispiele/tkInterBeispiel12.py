# GUIs mit tkInter - Bildbetrachter
# Alle Beispiele ohne Klasse, da das Thema erst am Abend 5 an die Reihe kommt

# Es gibt noch etwas zu tun:
# 1) Wie kann die Größe des Bildes automatisch angepasst werden?
# 2) Als Dateityp soll in der Dateityp-Auswahl auch png angeboten werden
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

currentImage = None

def DateiOeffnen():
    # Lösung 2: Die Variable muss per global zugänglich gemacht werden
    global currentImage
    filePath = filedialog.askopenfile(initialdir = "/", title="Wähle ein Bild",
     filetypes = (("Jpeg-Dateien","*.jpg"),("Alle Dateien","*.*")))
    # PhotoImage-Objekt aus dem Modul ImageTk anlegen
    img = ImageTk.PhotoImage(file=filePath.name)
    cav.create_image(0,0,image=img,anchor=tk.NW)
    # Lösung 1: Damit das img-Objekt nicht gleich wieder aufgeräumt wird, muss es "irgendwo" abgespeichert werden
    # currentImage = img

def Beenden():
    win.destroy()

win = tk.Tk()
win.title("tkInter - Beispiel Nr. 12")
win.geometry("600x400")

mainMenu = tk.Menu(win)
win.config(menu=mainMenu)

# tearoff = 0 - Ohne horizontalen Teiler
fileMenu = tk.Menu(mainMenu,tearoff=0)
fileMenu.add_command(label="Öffnen",command=DateiOeffnen)
fileMenu.add_separator()
fileMenu.add_command(label="Beenden",command=Beenden)

mainMenu.add_cascade(label="Bilder", menu=fileMenu)
cav = tk.Canvas(win)
# Canvas soll die ganze Breite einnehmen
cav.pack(fill=tk.BOTH, expand=1)

win.mainloop()

