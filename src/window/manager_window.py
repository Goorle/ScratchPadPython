from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QMainWindow
from design.main_window import Ui_MainWindow
import sys



class ManagerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManagerWindow()
    window.show()
    app.exec()