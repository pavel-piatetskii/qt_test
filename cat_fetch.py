import sys
from PySide6 import QtCore, QtWidgets, QtNetwork

class MyWidget(QtWidgets.QWidget):

  def __init__(self):

    super().__init__()

    # Add Button
    self.button = QtWidgets.QPushButton("Get a fact!")
    # Add text Label alligned at the window center
    self.text = QtWidgets.QLabel("Click a button to get a random fact about cats", 
                                  alignment=QtCore.Qt.AlignCenter)

    # Create layout for widgets, 'V' means 'align vertically'
    self.layout = QtWidgets.QVBoxLayout(self)
    self.layout.addWidget(self.text)
    self.layout.addWidget(self.button)

    self.button.clicked.connect(self.get_fact)

  # Create slot for a function next to it, that lets the function
  # to work as a callback function somewhere 
  # (https://doc.qt.io/qt-5/signalsandslots.html)
  @QtCore.Slot()
  def get_fact(self):
    url = "https://catfact.ninja/fact"
    request = QtNetwork.QNetworkRequest(QtCore.QUrl(url))

    self.nam = QtNetwork.QNetworkAccessManager()
    self.nam.finished.connect(self.response_handler)
    self.nam.get(request)


  def response_handler(self, reply):
    err = reply.error()

    if err == QtNetwork.QNetworkReply.NoError:
      #self.text.setText(reply)
      print(reply)

    else:
      print("Error occured: ", err)
      print(reply.errorString())

# Next 'if' prevents code from instant running if imported to somewhere
if __name__ == "__main__":
  app = QtWidgets.QApplication([])

  widget = MyWidget()
  widget.resize(400, 300)
  widget.show()

  sys.exit(app.exec())
