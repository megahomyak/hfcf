from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
import threading
import os
from fuzzyfinder import fuzzyfinder
import subprocess

low_map = {
    k: v
    for k, v in zip(
        "йцукенгшщзхъфывапролджэячсмитьбю.",
        "qwfpgjluy;[]arstdhneio'zxcvbkm,./",
    )
}

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
        self.modules = os.listdir("modules")
        self.uppers = {}
        for module in self.modules:
            uppers = ""
            for c in module:
                if c.isupper():
                    uppers += c
            if uppers:
                self.uppers[uppers] = module
        self.is_hot = True
        self.invocation.connect(self.process_invocation)
        self.set_prompt("")
    def set_prompt(self, prompt):
        results = []
        if not prompt:
            results = self.modules
        elif self.is_hot:
            try:
                module = self.uppers[prompt]
            except KeyError:
                for uppers, module in self.uppers.items():
                    if uppers.startswith(prompt):
                        results.append(module)
            else:
                subprocess.Popen([os.path.join("modules", module)], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.hide()
                self.set_prompt("")
                return
        else:
            results = list(fuzzyfinder(prompt, self.modules, ignore_case=False))
        self.prompt = prompt
        text = ""
        if self.is_hot:
            text += "HOT"
        else:
            text += "FUZZ"
        text += ": "
        text += prompt
        text += "\n\n"
        text += "\n".join(results)
        self.text.setText(text)
        self.text.adjustSize()
    def process_invocation(self):
        if self.isVisible():
            self.hide()
        else:
            self.showFullScreen()
    def keyPressEvent(self, event):
        new = low_map.get(event.text().lower(), event.text())
        if event.key() == Qt.Key.Key_Escape:
            self.set_prompt("")
        elif new == "/":
            self.is_hot = not self.is_hot
            self.set_prompt("")
        elif event.key() == Qt.Key.Key_Backspace:
            self.set_prompt(self.prompt[:-1])
        else:
            if self.is_hot or event.text() == event.text().upper():
                new = new.upper()
            self.set_prompt(self.prompt + new)

def main():
    def check_for_invocation():
        while True:
            with open("invoke") as f:
                f.read()
                window.invocation.emit()

    app = QApplication([])
    window = HFCFWindow()
    threading.Thread(target=check_for_invocation).start()
    app.exec()

main()
