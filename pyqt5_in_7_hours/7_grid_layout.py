import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QGridLayout, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)

        vbox_outer = QVBoxLayout()
        grid_inner = QGridLayout()

        self.text_output = QLabel("Click a button to change this text")
        self.text_output.setStyleSheet("font-size:20pt")
        self.text_output.setAlignment(Qt.AlignCenter)
        vbox_outer.addWidget(self.text_output)

        for i in range(0, 8):
            btn = QPushButton(f"Click {i+1}")

            # Proper way to create connection to a function inside a loop
            # k stores the value of i at the moment of creation
            # if i is not declared as argument, k will always be 1
            # if only i is used, without k, function will output only the last i in the loop
            btn.clicked.connect(lambda i, k=i: self.click_btn(k+1))
            grid_inner.addWidget(btn, i // 4, i % 4)
        vbox_outer.addLayout(grid_inner)
        self.setLayout(vbox_outer)

    def click_btn(self, n):
        self.text_output.setText(f"Button {n} clicked")


app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
