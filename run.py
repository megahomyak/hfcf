from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class HFCFWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("test")

        self.setCentralWidget(button)

app = QApplication([])
window = HFCFWindow()
window.show()
app.exec()
