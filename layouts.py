from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication


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
        self.setWindowTitle('Layouts in PySide')
        component_with_background = Color('red')
        self.setCentralWidget(component_with_background)

if __name__ == '__main__':
    app = QApplication([])
    window = PrincipalWindow()
    window.show()
    app.exec()