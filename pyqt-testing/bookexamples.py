import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("App")

        button = QPushButton("Press Me!")

        self.setCentralWidget(button)

app = QApplication([])

window = MainWindow()
window.show()

app.exec()