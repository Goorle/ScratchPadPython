from PyQt5.QtWidgets import QApplication, QDialog
from .design.authorization import Ui_AuthorizaionWindow
import sys

class Authorization(QDialog, Ui_AuthorizaionWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Authorization()
    window.show()
    app.exec()