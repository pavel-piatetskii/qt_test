from PyQt5.QtWidgets import QWidget
from ui.HelloWorldUI import Ui_Form

class HelloWorld(Ui_Form, QWidget):
    def __init__(self):
        super(HelloWorld, self).__init__()
        self.setupUi(self)