from PySide6.QtWidgets import QMainWindow, QApplication, QDial


class Components(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Components')
        component = QDial()
        # component = QSlider(Qt.Horizontal)
        # component.setMinimum(-25)
        # component.setMaximum(25)
        component.setRange(-25, 25)
        component.valueChanged.connect(self.change_value)
        component.sliderMoved.connect(self.slider_moved)
        component.sliderPressed.connect(self.slider_pressed)
        component.sliderReleased.connect(self.slider_released)
        self.setCentralWidget(component)

    def change_value(self, new_value):
        print(f'New value: {new_value}')

    def slider_moved(self, new_position):
        print(f'New position: {new_position}')

    def slider_pressed(self):
        print('Dial pressed')

    def slider_released(self):
        print('Dial released')

if __name__ == '__main__':
    app = QApplication([])
    window = Components()
    window.show()
    app.exec()