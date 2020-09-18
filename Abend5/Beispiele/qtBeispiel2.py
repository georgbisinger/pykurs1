# Qt-Beispiel 2: Ein Dialogfeld für die Eingabe eines Namens

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
        self.txeName = QLineEdit("<Name>", self)
        self.txeName.move(10, 60)
        self.txeName.resize(200, 30)

        btnOK = QPushButton("OK", self)
        btnOK.move(10, 140)
        btnOK.resize(160, 30)
        btnOK.clicked.connect(self.OKClick)


    def OKClick(self):
        print("Dein Name ist %s" % self.txeName.text())
        qtApp.quit()

qtApp = QtWidgets.QApplication([])
fenster = QtFenster()
fenster.show()

sys.exit(qtApp.exec_())