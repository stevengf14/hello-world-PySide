import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class PrincipalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals and Slots')
        self.setFixedSize(400, 200)
        self.tag = QLabel()
        self.text = QLineEdit()
        self.text.textChanged.connect(self.tag.setText)
        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.tag)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication([])
    window = PrincipalWindow()
    window.show()
    sys.exit(app.exec())