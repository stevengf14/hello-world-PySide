from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QHBoxLayout, QVBoxLayout


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
        horizontal_layout = QHBoxLayout()
        vertical_layout = QVBoxLayout()

        vertical_layout.addWidget(Color('yellow'))
        vertical_layout.addWidget(Color('blue'))
        vertical_layout.addWidget(Color('red'))
        horizontal_layout.addLayout(vertical_layout)
        horizontal_layout.addWidget(Color('green'))
        horizontal_layout.addWidget(Color('black'))
        component = QWidget()
        component.setLayout(horizontal_layout)
        self.setCentralWidget(component)

if __name__ == '__main__':
    app = QApplication([])
    window = PrincipalWindow()
    window.show()
    app.exec()