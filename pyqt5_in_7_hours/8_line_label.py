import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont
from PyQt5 import uic

class LabelLineUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("8_line_and_label.ui", self)
        self.findChild(QPushButton, "pushButton").clicked.connect(self.set_name)

        style_s = "background-color: blue; color: red;"

        self.result_label = self.findChild(QLabel, "labelResult")
        self.result_label.setFont(QFont("Sanserif", 15))
        self.result_label.setStyleSheet(style_s)

    def set_name(self):
        name = self.findChild(QLineEdit, "lineEdit").text()
        self.result_label.setText(name)


app = QApplication(sys.argv)
window = LabelLineUI()
window.show()
app.exec_()
