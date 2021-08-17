import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic

class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("3_my_button.ui", self)

        # Find our widgets

        button = self.findChild(QPushButton, "pushButton")
        button.clicked.connect(self.clicked_btn)

    def clicked_btn(self):
        print("Button Clicked")


app = QApplication([])
window = UI()
window.show()
app.exec_()
