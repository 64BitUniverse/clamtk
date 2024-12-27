import sys, os
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QWidget,
    QToolButton
)
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
basedir = os.path.dirname(__file__)

class UIAbout(QWidget):
    def __init__(self, parent=None):
        super(UIAbout, self).__init__(parent)
        self.ui = loader.load(
            os.path.join(basedir, "about.ui"), None
        )
        self.ui.setWindowTitle("About")
        
        self.Close = self.ui.findChild(QPushButton, "Close")
        self.Close.clicked.connect(self.closeEvent)

    def closeEvent(self):
        sys.exit(0)
        
class MainMenu(QMainWindow):
    def __init__(self, parent=None):
        super(MainMenu, self).__init__(parent)
        self.ui = loader.load(
            os.path.join(basedir, "mainmenu.ui"), None
        )
        self.ui.show()
        self.ui.setWindowTitle("MainMenu Title")

        self.about = self.ui.findChild(QToolButton, "About")
        self.about.clicked.connect(self.onClick)

    def onClick(self, is_checked):
        w = UIAbout()
        w.ui.show()




app = QApplication(sys.argv)
window = MainMenu()
app.exec()