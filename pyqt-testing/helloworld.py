import sys
import random
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QIcon

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ClamAV GUI")
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.bSettings = QtWidgets.QPushButton("Click me!")
        self.bSettings.setIcon(QIcon.fromTheme('preferences-system'))
        self.bSettings.setIconSize(self.bSettings.sizeHint() * 0.5)
        self.bSettings.setFixedSize(100,50)

        self.bSettings.setStyleSheet(
            "QPushButton { text-align: center; }"
            "QPushButton::icon { alignment: top; }"
        )

        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.bSettings)

        self.bSettings.clicked.connect(self.magic)
    
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())