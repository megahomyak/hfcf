from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
import threading

class HFCFWindow(QMainWindow):
    invocation=pyqtSignal()

    def __init__(self):
        super().__init__()
        self.text = QLabel(self)
        self.text.setTextFormat(Qt.TextFormat.PlainText)
        self.text.move(15, 15)
        self.setStyleSheet("background-color: black;")
        font = self.text.font()
        font.setPointSize(30)
        font.setFamily("Monospace")
        self.text.setFont(font)
        self.text.setStyleSheet("color: white;")
        self.invocation.connect(self.process_invocation)
        self.set_prompt("")
    def set_prompt(self, prompt):
        self.prompt = prompt
        text = prompt + "\n\na"
        self.text.setText(text)
        self.text.adjustSize()
    def process_invocation(self):
        if self.isVisible():
            self.hide()
        else:
            self.showFullScreen()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.set_prompt("")
        elif event.key() == Qt.Key.Key_Backspace:
            self.set_prompt(self.prompt[:-1])
        else:
            self.set_prompt(self.prompt + event.text().upper())

def check_for_invocation():
    while True:
        with open("invoke") as f:
            f.read()
            window.invocation.emit()

app = QApplication([])
window = HFCFWindow()
threading.Thread(target=check_for_invocation).start()
app.exec()
