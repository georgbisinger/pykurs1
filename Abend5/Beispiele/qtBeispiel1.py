# Qt-Beispiel 1: Das "absolute" Mininum

import sys
from datetime import datetime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton
from PyQt5.QtCore import QSize

class QtFenster(QMainWindow):
    global qtApp

    def __init__(self):
        super().__init__()

        # Fenstergröße und Titel festlegen
        self.setMinimumSize(QSize(400, 200))
        self.setWindowTitle("Hallo, Qt!")
        heute = "Uhrzeit: %s" % datetime.today().strftime("%H.%M")
        labelName = QLabel(heute, self)
        labelName.move(10, 10)
        btnOK = QPushButton("OK", self)
        btnOK.move(10, 40)
        btnOK.clicked.connect(self.OKClick)

    def OKClick(self):
        qtApp.quit()

qtApp = QtWidgets.QApplication([])
fenster = QtFenster()
fenster.show()

sys.exit(qtApp.exec_())