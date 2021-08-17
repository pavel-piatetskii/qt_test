import sys
import ast
from PyQt5 import QtCore, QtWidgets, QtNetwork

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
  # to work as a callback function
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
      # Read the reply string (b'), take data from it, decode the data as a utf-8 string
      reply_str = reply.readAll().data().decode("utf-8")
      # Convert a string to a dictionary
      reply_dict = ast.literal_eval(reply_str)
      # Change text in the text field
      self.text.setText(reply_dict['fact'])

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
