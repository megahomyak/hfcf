from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit

class HFCFWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        inputfield = QLineEdit()

        self.setCentralWidget(inputfield)

app = QApplication([])
window = HFCFWindow()
window.showFullScreen()
app.exec()
