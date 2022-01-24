import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class PrincipalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals and Slots')
        # Button
        button = QPushButton('Click here')
        button.setCheckable(True)
        button.clicked.connect(self.check_event)
        button.clicked.connect(self.click_event)
        self.setCentralWidget(button)

    def click_event(self):
        print('Clicked')

    def check_event(self, check):
        print(f'Checked? {check}')

if __name__ == '__main__':
    app = QApplication([])
    window = PrincipalWindow()
    window.show()
    sys.exit(app.exec())