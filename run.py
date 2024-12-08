from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtCore import Qt
import socket

invoker = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
invoker.bind("invoke")
try:
    class HFCFWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.inputfield = QLineEdit(self)
            font = self.inputfield.font()
            font.setPointSize(30)
            self.inputfield.setFont(font)
        def resizeEvent(self, event):
            self.inputfield.resize(self.width() - 30, 60)
            self.inputfield.move(15, 15)
            super().resizeEvent(event)
        def keyPressEvent(self, event):
            if event.key() == Qt.Key.Key_Escape:
                self.hide()
            else:
                super().keyPressEvent(event)

    app = QApplication([])
    window = HFCFWindow()
    window.show()
    app.exec()
finally:
    invoker.close()
