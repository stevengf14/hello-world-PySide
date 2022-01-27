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
        horizontal_layout.setContentsMargins(10,10,10,10)
        vertical_layout = QVBoxLayout()
        vertical_layout.setContentsMargins(5,10,5,10)

        vertical_layout.setSpacing(5)
        horizontal_layout.setSpacing(20)

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