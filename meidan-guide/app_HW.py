import sys
from PyQt5.QtWidgets import QApplication
from pages.HelloWorld import HelloWorld

if __name__ == "__main__":
    app = QApplication(sys.argv)

    HelloWorld = HelloWorld()
    HelloWorld.show()

    sys.exit(app.exec_())
