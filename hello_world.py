import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):

  def __init__(self):

    super().__init__()

    self.hello = ["Hello World", "Hallo Welt", "Hei maailma", 
                  "Hola Mundo", "Привет мир"]

    # Add Button
    self.button = QtWidgets.QPushButton("Click Me!")
    # Add text Label alligned at the window center
    self.text = QtWidgets.QLabel("Hello World", 
                                  alignment=QtCore.Qt.AlignCenter)

    # Create layout for widgets, 'V' means 'align vertically'
    self.layout = QtWidgets.QVBoxLayout(self)
    self.layout.addWidget(self.text)
    self.layout.addWidget(self.button)

    self.button.clicked.connect(self.switch_lang)

  # Create slot for a function next to it, that lets the function
  # to work as a callback function somewhere 
  # (https://doc.qt.io/qt-5/signalsandslots.html)
  @QtCore.Slot()
  def switch_lang(self):
    self.text.setText(random.choice(self.hello))

# Next 'if' prevents code from instant running if imported to somewhere
if __name__ == "__main__":
  app = QtWidgets.QApplication([])

  widget = MyWidget()
  widget.resize(400, 300)
  widget.show()

  sys.exit(app.exec())
