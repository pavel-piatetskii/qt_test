import sys
from PySide6 import QtCore, QtWidgets, QtNetwork
import socket

class MyWidget(QtWidgets.QWidget):

  def __init__(self):

    super().__init__()

    # Add Button
    self.button = QtWidgets.QPushButton("Send message")
    # Add field to enter message
    self.text_field = QtWidgets.QLineEdit()
    self.label = QtWidgets.QLabel("Message sender", alignment=QtCore.Qt.AlignTop)

    # Create layout for widgets, 'V' means 'align vertically'
    self.layout = QtWidgets.QVBoxLayout(self)
    self.layout.addWidget(self.label)
    self.layout.addWidget(self.text_field)
    self.layout.addWidget(self.button)

    self.button.clicked.connect(self.send_message)

  # Create slot for a function next to it, that lets the function
  # to work as a callback function 
  # (https://doc.qt.io/qt-5/signalsandslots.html)
  @QtCore.Slot()
  def send_message(self):
    # url = "localhost:8000"
    # text = QtCore.QByteArray(self.text_field.text())
    # request = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
    # self.nam = QtNetwork.QNetworkAccessManager()
    # self.nam.finished.connect(self.response_handler)
    # print(text)
    # self.nam.send(request, text)
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8000
    #BUFFER_SIZE = 1024
    message = self.text_field.text().encode("utf-8")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(message)
    #data = s.recv(BUFFER_SIZE)
    s.close()
    print("Sending message: ", message)



  def response_handler(self, reply):
    err = reply.error()

    if err == QtNetwork.QNetworkReply.NoError:
      print("x")

    else:
      print("Error occured: ", err)
      print(reply.errorString())

# Next 'if' prevents code from instant running if imported to somewhere
if __name__ == "__main__":
  app = QtWidgets.QApplication([])

  widget = MyWidget()
  widget.resize(300, 100)
  widget.show()

  sys.exit(app.exec())
