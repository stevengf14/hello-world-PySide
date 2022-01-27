from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QGridLayout, QStackedLayout


class Color(QWidget):
    def __init__(self, new_color):
        super().__init__()
        self.setAutoFillBackground(True)
        colors_palette = self.palette()
        colors_palette.setColor(QPalette.Window, QColor(new_color))
        self.setPalette(colors_palette)

class PrincipalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QStackedLayout()
        layout.addWidget(Color('yellow'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('red'))
        layout.setCurrentIndex(2)

        component = QWidget()
        component.setLayout(layout)
        self.setCentralWidget(component)

if __name__ == '__main__':
    app = QApplication([])
    window = PrincipalWindow()
    window.show()
    app.exec()