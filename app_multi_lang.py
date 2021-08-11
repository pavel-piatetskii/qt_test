import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator
from pages.MultiLang import MultiLang

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # language = config_read('language')
    language = sys.argv[1]

    trans = QTranslator()
    trans.load(f"./appLang_{language.upper()}.qm")
    # config_write('language', f""
    app.installTranslator(trans)

    MultiLang = MultiLang()
    MultiLang.show()

    sys.exit(app.exec_())
