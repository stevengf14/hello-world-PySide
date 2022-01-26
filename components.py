from PySide6.QtWidgets import QMainWindow, QApplication, QSpinBox, QDoubleSpinBox


class Components(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Components')
        number = QDoubleSpinBox()
        # number.setMinimum(-5)
        # number.setMaximum(5)
        number.setRange(-25.5, 25.5)
        number.setPrefix('$')
        number.setSuffix(' or USD')
        number.setSingleStep(3.5)
        number.valueChanged.connect(self.change_value)
        number.textChanged.connect(self.change_text)
        self.setCentralWidget(number)

    def change_value(self, new_value):
        print(f'New value: {new_value}')

    def change_text(self, new_text):
        print(f'New text: {new_text}')

if __name__ == '__main__':
    app = QApplication([])
    window = Components()
    window.show()
    app.exec()