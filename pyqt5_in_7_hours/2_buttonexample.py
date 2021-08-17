import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # super(WindowExample, self).__init__() - another way of accessing the parent class constructor

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Button example app")
        self.setWindowIcon(QIcon('1_icon_for_2nd.png'))

        self.createbuttons()

        # self.show()

    def createbuttons(self):
        btn1 = QPushButton("Click me", self)
        # btn1.move(0, 200)  # Move widget to a position on a parent widget
        btn1.setGeometry(100, 100, 75, 75)  # shorthand for sizing and positioning (posx, posy, sizex, sizey)
        btn1.setStyleSheet('color:red')
        btn1.setStyleSheet('background-color:white')

        btn2 = QPushButton("Click Two", self)
        btn2.setGeometry(175, 100, 75, 75)
        btn2.setIcon(QIcon("1_icon_for_2nd.png"))  # Icon can be set for a button as well
        btn2.setStyleSheet('color:#FF00FF')
        btn2.setStyleSheet('background-color:grey')


app = QApplication(sys.argv)
window = Window()
window.show()  # another way of showing  a window
sys.exit(app.exec_())
