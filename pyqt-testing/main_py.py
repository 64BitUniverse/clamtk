import sys, os
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QToolButton
)

from mainmenu_ui import Ui_MainWindow
from about_ui import Ui_About

class About(QWidget, Ui_About):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Close.pressed.connect(self.closeOnClick)
    
    def closeOnClick(self):
        self.a = None


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.a = None
        self.About.pressed.connect(self.onClick)
    def onClick(self):
        if self.a is None:
            self.a = About()
            self.a.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec()