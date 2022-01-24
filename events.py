import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class PrincipalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals and Slots')
        # Button
        button = QPushButton('Click here')
        button.clicked.connect(self.click_event)
        self.setCentralWidget(button)

    def click_event(self):
        print('Clicked')

if __name__ == '__main__':
    app = QApplication([])
    window = PrincipalWindow()
    window.show()
    sys.exit(app.exec())