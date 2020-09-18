# Qt-Beispiel 3: Ein Dialogfeld für die Eingabe eines Namens und einer E-Mail-Adresse

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton,  QLineEdit
from PyQt5.QtCore import QSize

class QtFenster(QMainWindow):
    global qtApp

    def __init__(self):
        super().__init__()

        # Fenstergröße und Titel festlegen
        self.setMinimumSize(QSize(600,300))
        self.setWindowTitle("Eingabe-Dialog")

        labelName = QLabel("Name:", self)
        # labelName.setAlignment(QtCore.Qt.AlignLeft)
        labelName.move(10, 10)

        labelEMail = QLabel("E-Mail:", self)
        # labelEMail.setAlignment(QtCore.Qt.AlignLeft)
        labelEMail.move(10, 100)

        texteditName = QLineEdit("<Name>", self)
        texteditName.move(120, 10)
        texteditName.resize(300, 30)

        texteditMail = QLineEdit("<EMail-Adresse>", self)
        texteditMail.move(120, 100)
        texteditMail.resize(300, 30)

        okButton = QPushButton("OK", self)
        okButton.move(10, 240)
        okButton.clicked.connect(self.OKClick)

        abrechenButton = QPushButton("Abbrechen", self)
        abrechenButton.move(120, 240)
        abrechenButton.clicked.connect(self.AbbrechenClick)


    def OKClick(self):
        print("OK-Button")
        qtApp.quit()

    def AbbrechenClick(self):
        print("Abbrechen-Button")
        qtApp.quit()

qtApp = QtWidgets.QApplication([])
fenster = QtFenster()
fenster.show()

sys.exit(qtApp.exec_())