import sys, os
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget
)
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
basedir = os.path.dirname(__file__)

class MainMenu():
    def __init__(self):
        super().__init__()
        self.ui = loader.load(
            os.path.join(basedir, "mainmenu.ui"), None
        )
        self.ui.setWindowTitle("MainMenu Title")
        self.ui.show()

app = QApplication(sys.argv)
window = MainMenu()
app.exec()