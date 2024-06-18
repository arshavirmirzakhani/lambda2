from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lambda2")


app = QApplication(sys.argv)

window = MainWindow()
window.show() 

app.exec()