import sys
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class PrincipalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals and Slots')
        # Button
        self.button = QPushButton('Click here')
        self.button.clicked.connect(self.click_event)
        self.windowTitleChanged.connect(self.title_changed)
        self.setCentralWidget(self.button)

    def click_event(self):
        self.button.setText('New Text')
        self.setEnabled(False)
        self.setWindowTitle('New App Title')
        print('Click event')

    def title_changed(self, new_title):
        print(f'New Title: {new_title}')

if __name__ == '__main__':
    app = QApplication([])
    window = PrincipalWindow()
    window.show()
    sys.exit(app.exec())