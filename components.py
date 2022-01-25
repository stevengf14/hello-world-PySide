from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication

class Components(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Components')
        tag = QLabel('Hi')
        tag.setText('Welcome')
        font = tag.font()
        # Default value = 12
        font.setPointSize(25)
        tag.setFont(font)
        # tag.setAlignment(Qt.AlignCenter)
        tag.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(tag)

if __name__ == '__main__':
    app = QApplication([])
    window = Components()
    window.show()
    app.exec()