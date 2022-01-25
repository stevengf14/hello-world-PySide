from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication

class Components(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Components')
        self.setFixedSize(500, 600)
        tag = QLabel('Hi')
        tag.setPixmap(QPixmap('spidey.jpg'))
        # tag.setScaledContents(True)
        self.setCentralWidget(tag)

if __name__ == '__main__':
    app = QApplication([])
    window = Components()
    window.show()
    app.exec()