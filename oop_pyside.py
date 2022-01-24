import sys
from PySide6.QtWidgets import QMainWindow, QApplication

class WindowPySide():
    def __init__(self):
        self.window = QMainWindow()
        self.window.setWindowTitle('OOP with PySide')
        self.window.resize(600, 400)

if __name__ == '__main__':
    app = QApplication([])
    # Create a window object
    window1 = WindowPySide()
    window1.window.show()
    # Execute window
    sys.exit(app.exec())
