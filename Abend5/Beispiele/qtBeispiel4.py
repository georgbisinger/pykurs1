# Qt-Beispiel 4: Ein Fenster mit Menü

import sys
import os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QMessageBox
from PyQt5.QtCore import QSize

class QtFenster(QMainWindow):
    global qtApp

    def __init__(self):
        super().__init__()
        # Icon-Pfade festlegen
        basePfad = os.path.dirname(__file__)
        newPfad = os.path.join(basePfad, "new.png")
        openPfad = os.path.join(basePfad, "open.png")
        closePfad = os.path.join(basePfad, "close.png")

        # Fenstergröße und Titel festlegen
        self.setMinimumSize(QSize(600,400))
        self.setWindowTitle("Fenster mit Menü")

        neuAktion = QAction(QIcon(newPfad), "&Neu", self)
        neuAktion.setShortcut("Ctrl+N")
        neuAktion.setStatusTip("Neues Dokument")
        neuAktion.triggered.connect(self.DokumentNeu)

        oeffnenAktion = QAction(QIcon(openPfad), "Ö&ffnen", self)
        oeffnenAktion.setShortcut("Ctrl+O")
        oeffnenAktion.setStatusTip("Dokument öffnen")
        oeffnenAktion.triggered.connect(self.DokumentOeffnen)

        endeAktion = QAction(QIcon(closePfad), "&Beenden", self)
        endeAktion.setShortcut("Ctrl+X")
        endeAktion.setStatusTip("Beenden")
        endeAktion.triggered.connect(self.Ende)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&Dateien")
        fileMenu.addAction(neuAktion)
        fileMenu.addAction(oeffnenAktion)
        fileMenu.addAction(endeAktion)

    def DokumentNeu(self):
        QMessageBox.information(self, "Demo", "Ein Dokument wird neu angelegt")

    def DokumentOeffnen(self):
        QMessageBox.information(self, "Demo", "Ein Dokument wird geöffnet")

    def Ende(self):
        qtApp.quit()

    def AbbrechenClick(self):
        print("Abbrechen-Button")
        qtApp.quit()

qtApp = QtWidgets.QApplication([])
fenster = QtFenster()
fenster.show()

sys.exit(qtApp.exec_())