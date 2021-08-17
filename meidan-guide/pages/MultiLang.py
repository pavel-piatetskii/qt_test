from PyQt5.QtWidgets import QWidget
from ui.LangTestUI import Ui_Form

class MultiLang(Ui_Form, QWidget):
    def __init__(self):
        super(MultiLang, self).__init__()
        self.setupUi(self)