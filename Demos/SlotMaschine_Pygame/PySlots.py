# Ein kleiner Früchtespielautomat

import os
import random
import pygame

from pygame.locals import *
from tkinter import *
from tkinter import messagebox

# Farbkonstanten für alle Fälle
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

AppTitel = "Frutomat 0.1"

SlotBildH = 0
SlotBildB = 0
SpielfeldH = 0
SpielfeldB = 0

# Verzeichnispfad für die Bilddateien - die Bilddateien befinden sich im Unterverzeichnis Fruits
SpielkartenPfad =  os.path.dirname(os.path.abspath(__file__))
SpielkartenPfad = os.path.join(SpielkartenPfad, "Fruits")

# Alle Dateien in dem Verzeichnis in ein Array einlesen
Spielkarten = []
Imageliste = []

# Die Inhalte der drei Slot-Räder
Slot1 = ""
Slot2 = ""
Slot3 = ""

# Startguthaben festlegen
Guthaben = 200

# Einlesen aller Bilder
def BilderEinlesen():
    global Spielkarten
    for Spielkarte in os.listdir(SpielkartenPfad):
        if "Deckblatt" not in Spielkarte:
            Spielkarten.append(Spielkarte)
    AnzahlSpielkarten = len(Spielkarten)
    print(str(AnzahlSpielkarten) + " Spielkarten wurden eingelesen.") 

# Laden der Bitmaps
def ImageLaden():
    global Imageliste
    global SlotBildB, SlotBildH
    for Spielkarte in Spielkarten:
        SpielkartePfad = os.path.join(SpielkartenPfad, Spielkarte)
        Karte = pygame.image.load(SpielkartePfad)
        Karte.convert()
        Imageliste.append(Karte)
        AnzahlImages = len(Imageliste)
        # Platzhalter an den Anfang setzen
        Platzhalter = pygame.image.load(os.path.join(SpielkartenPfad, "Deckblatt.png"))
    Imageliste = [Platzhalter] + Imageliste
    AnzahlImages = len(Imageliste)
    # Abmessungen für ein Slotbild abfragen
    SlotBildB, SlotBildH = Imageliste[0].get_size()
    print(str(AnzahlImages) + " Images wurden geladen.") 

# Zeichnen des ersten Spielrades
def Spielrad1Zeichnen(Deckblatt):
    global SpielfeldB, SpielfeldH, SlotBildB, SlotBildH
    global Slot1
    # random.shuffle(Imageliste)
    if Deckblatt:
        r1 = -1
    else:
        r1 = random.randint(1, len(Spielkarten)-1)
    Slot1 = Spielkarten[r1]
    xPos = (SpielfeldB - (SlotBildB * 3)) / 2
    yPos = (SpielfeldH / 2) - SlotBildH
    # + 1 da das Deckblatt ausgelassen werden soll
    screen.blit(Imageliste[r1+1],(xPos, yPos))
    pygame.display.flip()
    return

# Zeichnen des ersten Spielrades
def Spielrad2Zeichnen(Deckblatt):
    global SpielfeldB, SpielfeldH, SlotBildB, SlotBildH
    global Slot2
    # random.shuffle(Imageliste)
    if (Deckblatt):
        r2 = -1
    else:
        r2 = random.randint(0, len(Spielkarten)-1)
    Slot2 = Spielkarten[r2]
    xPos = (SpielfeldB - (SlotBildB * 3)) / 2 + 160
    yPos = (SpielfeldH / 2) - SlotBildH
    # + 1 da das Deckblatt ausgelassen werden soll
    screen.blit(Imageliste[r2+1],(xPos, yPos))
    pygame.display.flip()
    return

# Zeichnen des ersten Spielrades
def Spielrad3Zeichnen(Deckblatt):
    global SpielfeldB, SpielfeldH, SlotBildB, SlotBildH
    global Slot3
    # random.shuffle(Imageliste)
    if (Deckblatt):
        r3 = -1
    else:
        r3 = random.randint(0, len(Spielkarten)-1)
    Slot3 = Spielkarten[r3]
    xPos = (SpielfeldB - (SlotBildB * 3)) / 2 + 320
    yPos = (SpielfeldH / 2) - SlotBildH
    # + 1 da das Deckblatt ausgelassen werden soll
    screen.blit(Imageliste[r3+1],(xPos, yPos))
    pygame.display.flip()
    return

# Ausgabe des Guthabens
def GuthabenAusgabe():
    global SlotFont
    GuthabenAusgabe = "Guthaben:         "
    GuthabenLabel = SlotFont.render(GuthabenAusgabe, True, BLACK, BLACK)
    screen.blit(GuthabenLabel, (100, 400))
    GuthabenAusgabe = "Guthaben: " + str(Guthaben)
    GuthabenLabel = SlotFont.render(GuthabenAusgabe, True, YELLOW, BLACK)
    screen.blit(GuthabenLabel, (100, 400))
    pygame.display.update()

# Ausgabe der Game Over-Meldung
def GameOver():
    # Fenster unsichtbar machen
    Tk().wm_withdraw() 
    messagebox.showinfo(AppTitel, "Dein Guthaben ist aufgebraucht - das Spiel ist vorbei.")

# Feststellen des Gewinns
def GewinnErmittlung():
    global Guthaben
    GewinnBetrag = 0
    # Prüfen auf zwei Gleiche
    if Slot1 == Slot2 or Slot1 == Slot3 or Slot1 == Slot3 or Slot2 == Slot3:
        GewinnBetrag = 50
    # Prüfen auf drei Gleiche
    if Slot1 == Slot2 and Slot1 == Slot3 and Slot1 == Slot3:
        GewinnBetrag = 250
    Guthaben += GewinnBetrag
    if Guthaben <= 0:
        GameOver()

# Pygame initialisieren
pygame.init()

# Bildschirm festlegen
screen = pygame.display.set_mode((640, 480))
# Spielfeldgröße abfragen
SpielfeldB, SpielfeldH = pygame.display.get_surface().get_size()

# Ausgabefläche festlegen
winSurface = pygame.Surface(screen.get_size())
winSurface = winSurface.convert()
winSurface.fill((0, 255, 255))
pygame.display.set_caption(AppTitel)

# Fonts festlegen für verschiedene Ausgaben
CaptionFont = pygame.font.SysFont("monospace", 48, 1) 
SlotFont = pygame.font.SysFont("monospace", 40, 0)

# Titel ausgeben
TitelLabel = CaptionFont.render(AppTitel, 1, (128, 128, 0))
screen.blit(TitelLabel, (100, 10))

# Bilddateien einlesen
BilderEinlesen()
# Liste der Bitmaps erstellen
ImageLaden()

# Meldung anzeigen
MeldungText = "Neues Spiel mit Eingabe von 'g', Ende mit Eingabe von 'q'"
MeldungText += "\n\nEin Einsatz kostet 20 Punkte."
MeldungText += "\n\nFür zwei Gleiche gibt es 50, für drei Gleiche 250 Punkte."
# Tk-Fenster soll unsichtbar sein
Tk().wm_withdraw() 
messagebox.showinfo(AppTitel, MeldungText)

# Spielräder anzeigen
Spielrad1Zeichnen(True)
Spielrad2Zeichnen(True)
Spielrad3Zeichnen(True)

# Spieluhr initialisieren
clock = pygame.time.Clock()

# Game loop starten
gameActive = True
while gameActive:
    # Bildwiederholrate setzen
    clock.tick(30)
    # Aufgetretene Ereignisse abfragen
    for event in pygame.event.get():
        # Soll das Programm beendet werden?
        if event.type == pygame.QUIT:
            gameActive=False
        # Gab es eine Tastatureingabe?
        if event.type == pygame.KEYDOWN:
            if event.key == K_g:
                # Neue Runde
                Guthaben -= 20
                # Timer starten
                StartZeit = pygame.time.get_ticks()
                while(True):
                    Spielrad1Zeichnen(False)
                    Spielrad2Zeichnen(False)
                    Spielrad3Zeichnen(False)
                    pygame.time.wait(100)
                    if pygame.time.get_ticks() > StartZeit + 1000:
                        break
                GewinnErmittlung()
                GuthabenAusgabe()
            if event.key == K_q:
                # Spielabbruch
                exit(0)
    pygame.display.flip()

# Programm beenden
pygame.quit()
