import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class WindowExample(QWidget):
    def __init__(self):
        super().__init__()
        # super(WindowExample, self).__init__() - another way of accessing the parent class constructor

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Second sample app")
        self.setWindowIcon(QIcon('icon_for_2nd.png'))

        # Prohibit resizing
        # self.setFixedWidth(400)
        # self.setFixedHeight(400)

        # Transparent window
        # self.setWindowOpacity(0.5)

        self.setStyleSheet('background-color:grey')

        self.show()


app = QApplication(sys.argv)
window = WindowExample()
sys.exit(app.exec_())
