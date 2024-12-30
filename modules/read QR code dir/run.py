from pyzbar.pyzbar import decode
from PIL import ImageGrab
import pyperclip

pyperclip.copy(decode(ImageGrab.grabclipboard())[0].data.decode())
