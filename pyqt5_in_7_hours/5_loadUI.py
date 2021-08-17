import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("5_vbox_layout.ui", self)


app = QApplication([])
window = UI()
window.show()
app.exec_()
